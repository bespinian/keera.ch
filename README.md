# Keera - static site

Plain static pages, no build step. Eighteen content `.html` files - six pages in
German at the root, English under `en/`, French under `fr/` - plus `404.html`,
the shared files under `assets/`, and `robots.txt`, `sitemap.xml`, `llms.txt`,
`CNAME` and the IndexNow key file at the root.

Edit the HTML by hand. A change to a page's shell - header, footer, contact
form, metadata - has to be made in all three language copies. `AGENTS.md` has
the content and design rules the pages are written to, and says which script
runs on which page.

## Deploy to GitHub Pages

`.github/workflows/deploy.yml` publishes the repo on every push to `main` (and
on manual dispatch). It copies the checkout into `_site/`, minus `.git/`,
`.github/`, `_site/` itself, `AGENTS.md` and `README.md`, and hands that to
`actions/upload-pages-artifact` and `actions/deploy-pages`. Nothing is
generated, so the deployed bytes are the committed bytes.

After the deploy, the workflow pings [IndexNow](https://www.indexnow.org/) with
the URLs of the pages the push changed (every page on a manual run). Bing
shares those pings with the other IndexNow engines, and ChatGPT search,
Copilot and DuckDuckGo answer from Bing's index. The key is the root file
`4f788c756ba49f94dc46567ec756122c.txt`, whose name and content are the key; it
is public by design. A failed ping is logged and does not fail the run.

Google does not take IndexNow. It reads `sitemap.xml`, which `robots.txt`
names; submit the sitemap once in Google Search Console and in Bing Webmaster
Tools, which is also where both report what they indexed.

Set-up, once, under **Settings -> Pages**:

- **Source: GitHub Actions**, not "Deploy from a branch".
- **Custom domain: `keera.ch`**, which is also what `CNAME` in the repo says.
  The two have to agree; deleting `CNAME` unpublishes the site from that name.
- **Enforce HTTPS: on**, once the certificate is issued.

DNS at the registrar: four `A` records for the apex at `185.199.108.153`,
`185.199.109.153`, `185.199.110.153` and `185.199.111.153` (plus the matching
`AAAA` records if the zone carries IPv6), and a `CNAME` for `www` pointing at
`<owner>.github.io.`. Pages then redirects `www.keera.ch` to the apex itself.

## What the host no longer does

The site used to sit on an Infomaniak Apache host, where `.htaccess` set the
response codes, the redirects and the cache lifetimes. GitHub Pages serves
static files and nothing else, so that file is gone and its five jobs landed as
follows:

- **The custom 404** needs no configuration: Pages serves a root `404.html` for
  any missing path, which is exactly what `ErrorDocument` did.
- **No directory listings** - Pages never lists a directory.
- **http and www onto `https://keera.ch`** is the "Enforce HTTPS" setting plus
  the `www` CNAME above.
- **The language redirect** moved into `assets/js/language.js`, on the German
  root only. It is client-side now, so it skips crawlers explicitly -
  `AGENTS.md` under **Languages** has the detail.
- **The cache lifetimes are gone.** Pages sends `Cache-Control: max-age=600` on
  everything and takes no configuration, so there is no long-lived asset cache;
  a ten-minute lifetime revalidates a changed asset on its own.
