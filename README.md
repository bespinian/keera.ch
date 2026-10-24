# Keera - static site

Hand-written static pages with no build step: twelve pages in German at the
root, the same twelve under `en/` and `fr/`, plus `404.html`, `assets/` and a
few root files. Edit the HTML directly, in all three languages. `AGENTS.md`
holds the content and design rules.

Preview with a server that resolves extensionless URLs, such as `npx serve`.

## Deploy

`.github/workflows/deploy.yml` runs on every push to `main`, or by hand. It
copies the repo, minus `.git/`, `.github/`, `AGENTS.md` and `README.md`, to
GitHub Pages unchanged.

It then pings [IndexNow](https://www.indexnow.org/) with the pages the push
changed (every page on a manual run), which reaches Bing and through it
ChatGPT search, Copilot and DuckDuckGo. The key is the public root file
`4f788c756ba49f94dc46567ec756122c.txt`. A failed ping does not fail the run.
Google ignores IndexNow and reads `sitemap.xml`; submit it once in Google
Search Console and Bing Webmaster Tools.

One-time set-up under **Settings -> Pages**:

- **Source: GitHub Actions.**
- **Custom domain: `keera.ch`**, matching `CNAME`. Deleting `CNAME` takes the
  site off the domain.
- **Enforce HTTPS: on.**

DNS: four `A` records for the apex at `185.199.108.153` to `185.199.111.153`
(plus `AAAA` if the zone has IPv6), and `www` as a `CNAME` to
`<owner>.github.io.`, which Pages redirects to the apex.

## Coming from Apache

The site used to run on Apache, configured by `.htaccess`. On Pages the root
`404.html` serves every missing path, directories are never listed, HTTPS and
`www` are handled by the settings above, and the language redirect is
`assets/js/language.js`. Cache lifetimes are gone: Pages sends
`max-age=600` on everything.
