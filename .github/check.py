#!/usr/bin/env python3
"""Checks the rules in AGENTS.md that a program can check, so nobody has to
remember them. Run from the repo root: `python3 .github/check.py`. The deploy
runs it first and stops on any failure. Standard library only; it reads the
site and changes nothing.

It covers the mechanical rules - copies that must match, strings that must be
shared, files and anchors that must exist. The content and design rules in
AGENTS.md still need a person."""

import glob
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

LANGS = {"de": "", "en": "en/", "fr": "fr/"}
SITE = "https://keera.ch/"
CSS = "assets/css/keera.css"
# Kept on purpose with no page using it; see the provider marks in AGENTS.md.
UNUSED_CLASSES_OK = {"provider-mark--wide"}

errors = []


def fail(where, msg):
    errors.append(f"{where}: {msg}")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def squash(s):
    return " ".join(s.split())


def text(s):
    """Visible text of a fragment, entities decoded, whitespace collapsed."""
    return squash(html.unescape(re.sub(r"<[^>]+>", "", s)))


class Page(HTMLParser):
    """Every start tag with its attributes, plus a tag/class/id skeleton of the
    body that leaves out the language switcher, whose links differ by design."""

    def __init__(self, src):
        super().__init__(convert_charrefs=True)
        self.tags, self.skeleton = [], []
        self._depth, self._lang_at = 0, None
        self.feed(src)

    def handle_starttag(self, tag, attrs):
        a = {k: (v if v is not None else "") for k, v in attrs}
        self.tags.append((tag, a))
        void = tag in ("img", "input", "link", "meta", "br", "source", "path",
                       "rect", "circle", "line", "polyline", "polygon", "use")
        if not void:
            self._depth += 1
        if self._lang_at is None and "lang" in a.get("class", "").split():
            self._lang_at = self._depth
        if self._lang_at is None and tag != "script":
            self.skeleton.append((tag, a.get("class", ""), a.get("id", "")))

    def handle_startendtag(self, tag, attrs):
        a = {k: (v if v is not None else "") for k, v in attrs}
        self.tags.append((tag, a))
        if self._lang_at is None:
            self.skeleton.append((tag, a.get("class", ""), a.get("id", "")))

    def handle_endtag(self, tag):
        if self._lang_at is not None and self._depth == self._lang_at:
            self._lang_at = None
        self._depth -= 1

    def find(self, tag, **want):
        return [a for t, a in self.tags if t == tag
                and all(a.get(k.replace("_", "-")) == v for k, v in want.items())]


def page_url(lang, name):
    slug = "" if name == "index.html" else name[: -len(".html")]
    return SITE + LANGS[lang] + slug


def graph(src):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
    return json.loads(m.group(1))["@graph"] if m else []


# ---------- the pages ----------
pages = {lang: sorted(os.path.basename(p) for p in glob.glob(LANGS[lang] + "*.html")
                      if os.path.basename(p) != "404.html")
         for lang in LANGS}
names = pages["de"]
if len(names) != 13:
    fail("site", f"{len(names)} German pages, expected thirteen")
for lang in ("en", "fr"):
    if pages[lang] != names:
        fail(LANGS[lang], f"pages differ from the German set: "
             f"{sorted(set(pages[lang]) ^ set(names))}")

src, parsed = {}, {}
for lang in LANGS:
    for name in names:
        path = LANGS[lang] + name
        if os.path.exists(path):
            src[path] = read(path)
            parsed[path] = Page(src[path])
src["404.html"] = read("404.html")
parsed["404.html"] = Page(src["404.html"])
content = [p for p in src if p != "404.html"]
llms = read("llms.txt")
css = read(CSS)
scripts_js = "\n".join(read(p) for p in glob.glob("assets/js/*.js"))


# ---------- markup ----------
for path, s in src.items():
    p = parsed[path]
    if re.search(r"<style[\s>]", s) or any("style" in a for _, a in p.tags):
        fail(path, "inline style or <style>; the design lives in keera.css")
    for t, a in p.tags:
        if t != "a" or "href" not in a:
            continue
        docs = a["href"].startswith("https://docs.keera.ch")
        if docs and (a.get("target") != "_blank" or a.get("rel") != "noopener"):
            fail(path, f'docs link {a["href"]} needs target="_blank" rel="noopener"')
        if not docs and "target" in a:
            fail(path, f'only docs links open a new tab: {a["href"]}')
    if path.count("/") == 0 and path != "404.html" and "ß" in text(s):
        fail(path, "ß in German copy; Swiss spelling uses ss")

# Scripts: google-tag.js on every content page, contact-form.js where there is
# a form, language.js on the German home page, nothing else; 404 runs none.
for path in src:
    p = parsed[path]
    got = sorted(os.path.basename(a["src"]) for a in p.find("script") if "src" in a)
    want = []
    if path != "404.html":
        want.append("google-tag.js")
        if p.find("form"):
            want.append("contact-form.js")
        if path == "index.html":
            want.append("language.js")
    if got != sorted(want):
        fail(path, f"scripts {got}, expected {sorted(want)}")

# Inline scripts are data only: the JSON-LD, and on every content page the
# same speculation rules, which 404.html leaves out with the rest.
rules = set()
for path, s in src.items():
    inline = re.findall(r"<script(?![^>]*\ssrc=)([^>]*)>(.*?)</script>", s, re.S)
    for attrs, body in inline:
        kind = re.search(r'type="([^"]+)"', attrs)
        if not kind or kind.group(1) not in ("application/ld+json", "speculationrules"):
            fail(path, f"inline <script{attrs}>; only JSON-LD and speculation rules")
    spec = [squash(b) for a, b in inline if 'type="speculationrules"' in a]
    if path == "404.html":
        if spec:
            fail(path, "speculation rules on 404.html, which runs no scripts")
    elif len(spec) != 1:
        fail(path, f"{len(spec)} speculation rules blocks, expected one")
    else:
        rules.add(spec[0])
        try:
            json.loads(spec[0])
        except ValueError as e:
            fail(path, f"speculation rules are not JSON: {e}")
if len(rules) > 1:
    fail("site", "speculation rules differ between pages")


# ---------- copies that must match ----------
def block(s, tag):
    m = re.search(rf"<{tag}[\s>].*?</{tag}\s*>", s, re.S)
    return m.group(0) if m else None


def lang_switcher(s):
    # AGENTS.md puts the switcher right before the menu checkbox.
    m = re.search(r'<span class="lang".*?(?=<input class="site-menu-state")', s, re.S)
    return m.group(0) if m else ""


for lang in LANGS:
    for tag, why in (("header", "header"), ("footer", "footer"), ("form", "form")):
        seen = {}
        for name in names:
            path = LANGS[lang] + name
            b = block(src.get(path, ""), tag)
            if b is None:
                continue
            b = b.replace(lang_switcher(b), "")
            b = re.sub(r'\s(aria-current="page"|checked)(?=[\s>/])', "", b)
            seen.setdefault(squash(b), []).append(name)
        if len(seen) > 1:
            groups = sorted(seen.values(), key=len)
            fail(LANGS[lang] or "de", f"{why} differs between pages: "
                 + " | ".join(", ".join(g) for g in groups))

for name in names:
    de = LANGS["de"] + name
    if de not in src:
        continue
    de_svgs = [squash(x) for x in re.findall(r"<svg.*?</svg\s*>", src[de], re.S)]
    for lang in ("en", "fr"):
        path = LANGS[lang] + name
        if path not in src:
            continue
        if parsed[path].skeleton != parsed[de].skeleton:
            a, b = parsed[de].skeleton, parsed[path].skeleton
            i = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
            fail(path, f"structure differs from {de} at element {i}: "
                 f"{a[i] if i < len(a) else 'end'} vs {b[i] if i < len(b) else 'end'}")
        svgs = [squash(x) for x in re.findall(r"<svg.*?</svg\s*>", src[path], re.S)]
        if svgs != de_svgs:
            fail(path, f"inline SVGs differ from {de}")

# The switcher: DE / FR / EN, the current language unlinked, the others
# pointing at this page in their language.
for lang in LANGS:
    for name in names:
        path = LANGS[lang] + name
        sw = lang_switcher(src.get(path, ""))
        labels = re.findall(r">\s*(DE|FR|EN)\s*<", sw)
        current = re.findall(r'<span aria-current="true">(DE|FR|EN)</span', sw)
        if labels != ["DE", "FR", "EN"] or current != [lang.upper()]:
            fail(path, f"switcher reads {labels}, current {current}")
        slug = "" if name == "index.html" else name[:-5]
        up = "../" if LANGS[lang] else ""
        for other in LANGS:
            if other != lang:
                href = up + LANGS[other] + slug
                if f'href="{href or "./"}"' not in sw:
                    fail(path, f"switcher has no link {href!r} to {other}")


# ---------- metadata ----------
canonicals = set()
for lang in LANGS:
    for name in names:
        path = LANGS[lang] + name
        if path not in src:
            continue
        s, p = src[path], parsed[path]
        head = s.split("</head>")[0]
        title = text(re.search(r"<title>(.*?)</title>", s, re.S).group(1))
        meta = lambda **k: (p.find("meta", **k) or [{}])[0].get("content")
        desc = meta(name="description")
        url = page_url(lang, name)
        canonicals.add(url)
        if len(title) > 65:
            fail(path, f"title is {len(title)} characters, keep it under about 65")
        if not desc or not 100 <= len(desc) <= 160:
            fail(path, f"description is {len(desc or '')} characters, keep it 100-160")
        if meta(property="og:description") != desc:
            fail(path, "og:description differs from the description")
        if meta(property="og:title") != title:
            fail(path, "og:title differs from <title>")
        if meta(property="og:url") != url:
            fail(path, f"og:url should be {url}")
        canon = p.find("link", rel="canonical")
        if [a["href"] for a in canon] != [url]:
            fail(path, f"canonical should be {url}")
        alts = {a["hreflang"]: a["href"] for a in p.find("link", rel="alternate") if "hreflang" in a}
        want = {l: page_url(l, name) for l in LANGS} | {"x-default": page_url("de", name)}
        if alts != want:
            fail(path, "hreflang links are not de, fr, en and x-default")
        for cut in ("space-grotesk-latin.woff2", "jetbrains-mono-latin.woff2"):
            if not any(a.get("href", "").endswith(cut) and "crossorigin" in a
                       for a in p.find("link", rel="preload")):
                fail(path, f"no crossorigin preload of {cut}")

        nodes = graph(s)
        descs = [n["description"] for n in nodes if "description" in n]
        if descs and desc not in descs:
            fail(path, "JSON-LD description differs from the description")
        if lang == "en" and desc and desc not in llms:
            fail(path, "description is not in llms.txt")

        # FAQPage mirrors the visible questions and answers.
        body = text(s.split("</head>", 1)[1])
        for n in nodes:
            if n.get("@type") != "FAQPage":
                continue
            for q in n["mainEntity"]:
                if text(q["name"]) not in body:
                    fail(path, f"FAQPage question not on the page: {q['name'][:60]}")
                elif text(q["acceptedAnswer"]["text"]) not in body:
                    fail(path, f"FAQPage answer not on the page: {q['name'][:60]}")

        # The hero preload names the hero <img> character for character.
        for pre in p.find("link", rel="preload", **{"as": "image"}):
            imgs = [a for a in p.find("img") if a.get("src") == pre["href"]]
            if not any(a.get("srcset") == pre.get("imagesrcset")
                       and a.get("sizes") == pre.get("imagesizes") for a in imgs):
                fail(path, f"image preload {pre['href']} does not match its <img>")

# Sitemap: every content URL once, with a lastmod, nothing else.
sitemap = read("sitemap.xml")
locs = re.findall(r"<url>\s*<loc>([^<]+)</loc>", sitemap)
if sorted(locs) != sorted(canonicals):
    fail("sitemap.xml", f"URLs differ from the pages: {sorted(set(locs) ^ canonicals)}")
if sitemap.count("<lastmod>") != len(locs):
    fail("sitemap.xml", "every URL needs one <lastmod>")
if re.search(r"<(changefreq|priority)>", sitemap):
    fail("sitemap.xml", "no <changefreq> or <priority>")


# ---------- links and files ----------
ids = {path: {a["id"] for _, a in parsed[path].tags if "id" in a} for path in src}


def resolve(base, href):
    """The repo file an internal link or asset reference points at, or None
    for links that leave the site."""
    if re.match(r"[a-z]+:|//", href) and not href.startswith(SITE):
        return None
    if href.startswith(SITE):
        href = "/" + href[len(SITE):]
    href = href.split("?")[0]
    if href.startswith("/"):
        target = href[1:]
    else:
        target = os.path.normpath(os.path.join(os.path.dirname(base), href))
        target = "" if target == "." else target
    if target == "" or target.endswith("/") or os.path.isdir(target):
        return os.path.join(target, "index.html")
    if not os.path.splitext(target)[1]:
        return target + ".html"
    return target


referenced = set()
for path in src:
    for t, a in parsed[path].tags:
        refs = [a[k] for k in ("href", "src") if k in a]
        refs += [a["content"] for k in ("og:image",) if a.get("property") == k]
        for k in ("srcset", "imagesrcset"):
            refs += [c.split()[0] for c in a.get(k, "").split(",") if c.strip()]
        for ref in refs:
            link, _, frag = ref.partition("#")
            target = path if not link else resolve(path, link)
            if target is None:
                continue
            target = os.path.normpath(target)
            referenced.add(target)
            if not os.path.isfile(target):
                fail(path, f"{ref} points at {target}, which does not exist")
            elif frag and target in ids and frag not in ids[target]:
                fail(path, f"{ref}: no id {frag!r} in {target}")
for m in re.finditer(r'url\("?\.\./([^")]+)', css):
    referenced.add(os.path.normpath("assets/" + m.group(1)))
for asset in glob.glob("assets/*/*"):
    if asset not in referenced and os.path.basename(asset) not in llms:
        fail(asset, "unused; the deploy mirrors the folder, so delete it")


# ---------- the stylesheet ----------
bare = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", bare):
    selector = squash(m.group(1))
    if re.search(r"#[0-9a-fA-F]{3,8}\b", m.group(2)) and selector not in (":root", ".theme-leaf"):
        line = bare[: m.start(2)].count("\n") + 1
        fail(CSS, f"hex colour in {selector} near line {line}; use a token")

css_classes = set(re.findall(r"\.([a-zA-Z][\w-]*)", re.sub(r'url\([^)]*\)|"[^"]*"', "", bare)))
html_classes = {c for p in parsed.values() for _, a in p.tags for c in a.get("class", "").split()}
for c in sorted(html_classes - css_classes):
    fail(CSS, f"class .{c} is in the markup but not the stylesheet")
for c in sorted(css_classes - html_classes - UNUSED_CLASSES_OK):
    if c not in scripts_js:
        fail(CSS, f"class .{c} is styled but used nowhere")


if errors:
    print("\n".join(errors))
    print(f"\n{len(errors)} problem(s).")
    sys.exit(1)
print(f"All checks passed: {len(src)} pages.")
