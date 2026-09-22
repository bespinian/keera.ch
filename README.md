# Keera - static site

Plain static pages, no build step. Eighteen content `.html` files - six pages in
German at the root, English under `en/`, French under `fr/` - plus `404.html`
and the shared files under `assets/`:

- `assets/css/keera.css` - the whole design layer. Markup carries classes only.
- `assets/js/contact-form.js` - the contact form's submit handler, on the nine
  pages with a form.
- `assets/js/google-tag.js` - the Google Ads tag, on all eighteen content pages.
- `assets/js/language.js` - the Accept-Language redirect, on `index.html` alone.
- `assets/fonts/`, `assets/img/` - woff2 subsets and artwork.

The one script that is not a local file is the hosted Simple Analytics tag,
`async` at the end of the body on all eighteen content pages. It is cookieless.
The site runs nothing else.

`robots.txt`, `sitemap.xml`, `llms.txt` and `CNAME` sit beside them at the root.
`CNAME` holds `keera.ch` and is what binds the custom domain to the deployment;
deleting it unpublishes the site from that name.

Edit the HTML by hand. A change to a page's shell - header, footer, contact
form, metadata - has to be made in all three language copies. `AGENTS.md` has
the content and design rules the pages are written to.

## Deploy to GitHub Pages

`.github/workflows/deploy.yml` publishes the repo on every push to `main` (and
on manual dispatch). It copies the checkout into `_site/`, minus `.git/`,
`.github/`, `AGENTS.md` and `README.md`, and hands that to
`actions/upload-pages-artifact` and `actions/deploy-pages`. Nothing is
generated, so the deployed bytes are the committed bytes.

Set-up, once, under **Settings -> Pages**:

- **Source: GitHub Actions**, not "Deploy from a branch".
- **Custom domain: `keera.ch`**, which is also what `CNAME` in the repo says.
  The two have to agree.
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
  any missing path, which is exactly what `ErrorDocument` did. `404.html` keeps
  its root-absolute URLs.
- **No directory listings** - Pages never lists a directory.
- **http and www onto `https://keera.ch`** is the "Enforce HTTPS" setting plus
  the `www` CNAME above.
- **The language redirect** moved into `assets/js/language.js`, which runs on
  the German root only. It negotiates once per session and never overrides a
  click that came from inside the site. Note that this is a client-side
  redirect: a crawler that executes JavaScript and reports `en-US` now follows
  it to `/en/`, where the Apache rule sent a header-less crawler to the German
  root. The `hreflang` and `x-default` links are unchanged.
- **The cache lifetimes are gone and cannot come back.** Pages sends
  `Cache-Control: max-age=600` on everything and takes no configuration, so the
  year-long `immutable` asset cache is no longer available. The
  `?v=<content hash>` stamping that paid for it - `fingerprint-assets.py` and
  its deploy step - has been removed with it, since a ten-minute lifetime
  already revalidates an asset that changed.
