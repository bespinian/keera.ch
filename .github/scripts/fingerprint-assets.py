#!/usr/bin/env python3
"""Stamp a content hash onto every asset URL, in place, before the upload.

No filename in this repo carries a content hash, so `?v=<hash>` is what makes an
asset URL change when its bytes do - which is what lets `.htaccess` cache assets
for a year. Deploy runs this; the repo keeps its plain URLs and only the uploaded
copy carries the stamps.

Run it from anywhere; it always rewrites the checkout it lives in. A second run
is a no-op, because any URL that already has a query string is skipped.
"""

import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

# HTML is deliberately absent: pages carry the stamps, so they have to stay
# revalidated or nobody ever learns a hash changed.
STAMPED = {".css", ".js", ".webp", ".jpg", ".jpeg", ".png", ".svg", ".woff2"}

HTML_REF = re.compile(r'\b(src|href)="([^"]*)"')
CSS_REF = re.compile(r'url\("([^"]*)"\)')

_digests: dict[pathlib.Path, str] = {}


def digest(path: pathlib.Path) -> str:
    """Eight hex characters of the file's SHA-256."""
    if path not in _digests:
        _digests[path] = hashlib.sha256(path.read_bytes()).hexdigest()[:8]
    return _digests[path]


def resolve(doc: pathlib.Path, url: str) -> pathlib.Path | None:
    """The file a URL points at, or None if this URL is not ours to stamp.

    Absolute URLs are skipped: the only ones here are the og:image and ld+json
    values, which crawlers read rather than the page loading them. A URL that
    already has a query or a fragment is skipped too, which is what makes a
    second run a no-op.
    """
    if not url or "://" in url or url.startswith(("data:", "mailto:", "#")):
        return None
    if "?" in url or "#" in url:
        return None
    if pathlib.PurePosixPath(url).suffix.lower() not in STAMPED:
        return None
    target = ROOT / url.lstrip("/") if url.startswith("/") else doc.parent / url
    try:
        target = target.resolve()
        target.relative_to(ROOT)
    except (OSError, ValueError):
        return None
    return target if target.is_file() else None


def stamp(doc: pathlib.Path, pattern: re.Pattern, group: int) -> int:
    original = doc.read_text()
    count = 0

    def replace(match: re.Match) -> str:
        nonlocal count
        url = match.group(group)
        target = resolve(doc, url)
        if target is None:
            return match.group(0)
        count += 1
        return match.group(0).replace(f'"{url}"', f'"{url}?v={digest(target)}"')

    text = pattern.sub(replace, original)
    if text != original:
        doc.write_text(text)
    return count


def find_unstamped(docs: list[pathlib.Path]) -> list[tuple[pathlib.Path, str]]:
    """Asset filenames left without a ?v= stamp.

    This searches for the filenames themselves rather than reusing the patterns
    above, so a regex that quietly stops matching cannot also stop reporting its
    own omissions.
    """
    names = sorted(
        {f.name for f in (ROOT / "assets").rglob("*") if f.is_file()},
        key=len, reverse=True,
    )
    missed = set()
    for doc in docs:
        text = doc.read_text()
        for name in names:
            for hit in re.finditer(re.escape(name), text):
                if text[hit.end():].startswith("?v="):
                    continue
                # og:image and the ld+json logo are absolute on purpose and
                # carry no stamp.
                if "https://keera.ch/" in text[max(0, hit.start() - 40):hit.start()]:
                    continue
                missed.add((doc.relative_to(ROOT), name))
    return sorted(missed)


def main() -> int:
    stylesheets = sorted(ROOT.glob("assets/css/*.css"))
    pages = sorted(p for p in ROOT.glob("**/*.html") if ".git" not in p.parts)

    # The stylesheet's own @font-face URLs have to be stamped before anything
    # hashes the stylesheet, or the CSS would go up under the digest of its
    # pre-rewrite self.
    fonts = sum(stamp(css, CSS_REF, 1) for css in stylesheets)
    assets = sum(stamp(page, HTML_REF, 2) for page in pages)

    missed = find_unstamped(stylesheets + pages)
    if missed:
        for doc, name in missed:
            print(f"BUG: left unstamped: {doc} -> {name}", file=sys.stderr)
        return 1

    print(f"stamped {assets} asset URLs across {len(pages)} pages "
          f"and {fonts} font URLs across {len(stylesheets)} stylesheets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
