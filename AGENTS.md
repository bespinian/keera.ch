# Keera Website

Thirty-six hand-written static pages - twelve in German at the root, the same
twelve under `en/` and `fr/` - plus `404.html`. No build step: every push to
`main` deploys the repo to GitHub Pages as committed (see the README).

## Ground rules

- Markup carries classes only. The whole design is `assets/css/keera.css`: no
  inline `style`, no per-page `<style>`, no client-side rendering. Read the
  stylesheet before adding a class; most sections need nothing new.
- Every page exists three times. A change to one language is a change to all
  three, and copies of shared markup (icons, logos, header, footer, form) stay
  identical.
- The site runs four scripts and no others: `contact-form.js` on pages with a
  form, `google-tag.js` and the hosted Simple Analytics tag on every content
  page, `language.js` on the German home page.
- A new third-party script, host or processor goes into `privacy.html`, in all
  three languages, before it ships.

## Design

- **Quiet.** One accent on a white or near-black ground, following the system
  scheme; there is no toggle. No gradients, glows or animation. Smooth anchor
  scrolling is the one motion, off under `prefers-reduced-motion`.
- **Every colour is a token.** Hex values live only in the token blocks
  (`:root`, its dark copy, the `.theme-leaf` hovers, `@media print`); anywhere
  else a hex is right in one scheme only. Partner and customer logos are the
  exception: their brand fills sit as `fill` attributes in the markup.
- **The accent is blue**, except on the three sustainability pages, where
  `class="theme-leaf"` on `<body>` swaps it for green. It is a swap: no page
  shows both, and no other page gets a theme class.
- **`.sprawl-void` and `.flow-branch` are the only other colours**, a pair:
  `--err` under `index.html#problem`, `--ok` under `gateway.html#architecture`.
  Move them together; do not add a third.
- **One idea per section**: a heading, at most two short paragraphs, then three
  or four short cards or one table. `gateway.html#features` is the one six-card
  section.
- **Simple language.** Short sentences, plain words. German _du_, English
  _you_, French _vous_.
- **Keera stays.** The mascot and the comic are the point of difference. Each
  product page has one diagram, and a diagram must say something the prose
  does not. Pricing, the model catalogue and the three legal pages have no
  artwork.
- **Do not add** logo strips, fake terminal sessions, benefit grids,
  integration cards, pricing outside `pricing.html`, hosted-model tables
  outside `models.html`, customer quotes or a light/dark screenshot toggle. Two
  rows look like logo strips and are not: the partners on
  `sovereignty.html#infrastructure` (the companies whose hardware Keera runs
  on, nobody else) and the customers under the home hero (real customers, each
  linked, nothing else).

## Positioning

- **Keera Gateway comes first** wherever the two products are listed: nav,
  footer, home cards, form checkboxes, sitemap, `llms.txt`, opening sentences.
  The gateway is the wedge - it also governs the models a customer already pays
  for - and Keera Engine is the next step.
- **Keera Engine is a model-agnostic inference engine** on open technology
  (Kubernetes, vLLM, llm-d). It runs any open model vLLM can serve; Keera's
  three fine-tunes are one option, never the offer. It sits _behind_ the
  gateway and is never called a client of it. Its efficiency claims stay with
  what vLLM and llm-d do. Nothing sells Keera as a coding agent or as a set of
  models.
- **Keera Chat** (`chat.keera.ch`) is part of the gateway, not a third product:
  a page and a nav item, but no home card, no form checkbox and no price.
- **Source-available, not open source.** The gateway and the chat are public
  on GitHub (`bespinian/keera-gateway`, `bespinian/keera-chat`) under the Keera
  Community Licence. Say the source can be _read_ and name the licence; never
  call either open source. Open source is the stack beneath: Kubernetes, vLLM,
  llm-d, the open-weight models. The footer's GitHub link points at the gateway
  repo, not the organisation.
- **Content, not record.** Wherever data handling comes up - the FAQs, the
  chat page, the terms - the prompt and the answer are never stored or trained
  on, while the request (who, when, which model, how many tokens, which
  decision) is kept in the customer's audit log. Never write "nothing is
  logged".
- **The docs** (`docs.keera.ch`, English, labelled _Docs_ everywhere) are the
  only links on the site that open in a new tab (`target="_blank"
  rel="noopener"`).

## Pages

What the markup does not already show.

- **`index.html`** - Four visuals, no more: the hero, the `.sprawl`, the
  `.stack` and comic page 1; the customer logos do not count. The customer row
  is a white band under the white hero, so the alternation from `#problem` down
  is untouched. `#problem` states the problem before naming the product, and
  its middle fact (cost control) sets up the Budgets row of `#solution`, a
  six-row `.stack`: one endpoint, not six features. Change the two together;
  `#solution`'s names are independent of `gateway.html#features`.
- **`gateway.html`** - `#security` is what the endpoint decides for the
  business, `#features` what the product is made of. The six feature names are
  the gateway repo's own: check it before rewording one. German and English keep
  them in English, French translates. The second paragraph of `#web-ui` is the
  page's only observability claim and stays; the caption says the figures come
  from a demo instance.
- **`engine.html`** - `#models` opens on "any open model vLLM can serve". Its
  mono footnote is load-bearing: the hosted providers (four Swiss, Mistral in
  the EU, Anthropic, OpenAI and Google in the USA, all in `models.html`) run on
  their own infrastructure, are blocked by default and are opened per team and
  data class. It carries the month it was checked: update the stamp when the sentence changes, and the
  sentence when a provider comes or goes. The models column of
  `gateway.html#architecture` says the same.
- **`chat.html`** - Short, because the docs carry the detail. No form; its
  three-question `#faq` is the last section.
- **`sovereignty.html`** - The argument is the gateway's; the engine is one
  backend behind it. The last column of `.layer-table` is in the accent because
  those cells are the argument. `#infrastructure` names no partner in its prose
  - the wordmarks do - so a new partner is one `<li>` in `.partners`. It claims
  only that the partners are Swiss and run data centres, GPUs and inference.
- **`pricing.html`** - Gateway only; Keera Engine has no price anywhere on the
  site. Three plans, in the order of `index.html#deploy`: Swiss Cloud (no base
  fee, a shared instance, model usage only), Dedicated (CHF 495 a month, CHF
  5’346 a year), Enterprise (on request, on the customer's infrastructure).
  Prices are per organisation; a yearly contract takes 10% off the base fee,
  never off model usage. Swiss Cloud alone is `.plan--start`, and its button
  and the hero's go to `gateway.keera.ch`; the other two go to `#contact`. In
  `.plan-table` a value several plans share is repeated in each column, never
  spanned. Plan names stay English in German and English; French says _Swiss
  Cloud_, _Dédié_, _Enterprise_. Numbers follow the language - `5’346`,
  `5,346`, `5&#x202F;346` - and the JSON-LD writes `5346`.
- **`models.html`** - The data is the gateway's. Regenerate the tables from
  `internal/catalog/providers.go` and the marks from `providerMarks` in
  `internal/webui/assets/ui.js` in the gateway repo, all three languages at
  once; never retype them. Prices are CHF per million tokens exactly as the
  gateway bills: never round, convert or discount. The Swiss providers come
  first (stepping stone, Infomaniak, Phoeniqs, CSCS), then Mistral in the EU,
  then Anthropic, OpenAI and Google in the USA. A provider the gateway marks
  `CachedInput` gets the cached-input column and its note. Rows keep the gateway's order and use its `DisplayName`. A starred row costs
  more for long prompts, and every starred row in one table must share the
  note's threshold and factor.
- **`sustainability.html`** - Swiss hosting is a fact here, not the argument.
  The refusal of a climate-neutral claim survives every rewrite, here and in the
  story.
- **The legal pages** (`imprint`, `terms`, `privacy`) - The site's own pages in
  all three languages, linked from the footer only, with no artwork and no
  _Start for free_ button. Change the `Stand` / `Last updated` / `Version du`
  date with the text. The imprint mirrors `bespinian.io/de/imprint` plus the UID
  (_IDE_ in French).

## Change together

- **A price**: the plan cards, `.plan-table`, the pricing description and
  JSON-LD (Dedicated's `MON` and `ANN` specifications), `llms.txt`, the Swiss
  Cloud line of `index.html#deploy`, and the payment band of `terms.html`.
- **A page description**: `<meta name="description">`, the JSON-LD and
  `llms.txt` share one string.
- **An FAQ**: the `FAQPage` node mirrors the prose on `gateway.html`,
  `engine.html`, `chat.html` and `sovereignty.html`; regenerate it from the
  markup.
- **A feature name**: the gateway's six `#features` `<h3>`s are its
  `featureList`; the engine's `featureList` restates its four `#what` layers.
- **A hero image**: the `<img>` `src`, `srcset` and `sizes` and the head
  preload's `href`, `imagesrcset` and `imagesizes`, character for character, or
  it downloads twice.
- **Comic copy**: a re-render of the artwork in three languages, plus the
  transcript.
- **The IndexNow key file** and the deploy step that names it; **`CNAME`** and
  the custom domain under Settings -> Pages.

## Languages

German (`de-CH`, Swiss spelling: `ss`, never `ß`) at the root, English (`en`)
under `en/`, French (`fr`) under `fr/`, all with the same English filenames.
Between copies only the prose differs, plus `../assets/...` and the switcher
links. Every page carries a DE/FR/EN switcher, always in that order with the
current language unlinked, and `hreflang` links for `de`, `fr`, `en` and
`x-default` (the German page).

`language.js` negotiates the entry point on the German home page only: `fr`
goes to `/fr/`, `de` or `gsw` stays, anything else goes to `/en/`. No language,
a referrer from this site, or a second arrival in the session never redirects.
A crawler (`navigator.webdriver`, or a user agent matching `bot`, `crawl`,
`spider`, `slurp`, `google`, `headless`) never redirects either, or it would
index `/en/` in place of the German root; keep that guard ahead of the language
check.

French puts `&nbsp;` before `:`, `;`, `?`, `!` and inside `«&nbsp;…&nbsp;»`. The
description and the JSON-LD share one string and a `<script>` decodes no
entities, so there it is a literal U+00A0. Keep these French terms stable:
_souveraineté_, _durabilité_, _poids ouverts_, _codage agentique_, _dépôt_,
_tenant_, _masquage_, _groupe_ (Omnivor), and _nLPD_ for revDSG.

## Header and footer

The header: wordmark, the nav, the switcher, and the login to
`gateway.keera.ch`. The nav is Gateway, Models, Chat, Inference, Pricing,
_Docs_, and an _About_ `details.nav-group` holding Sovereignty, Sustainability
and the story. The nav names the products without the brand (_Gateway_,
_Inference_ / _Inférence_, _Chat_); everywhere else says _Keera Gateway_,
_Keera Engine_, _Keera Chat_. The login is the header's one button - no other
CTA, no Contact link. It is in the markup twice, `a.header-login` and the phone
menu's `a.nav-login`, and exactly one is visible.

The phone menu is a hidden `.site-menu-state` checkbox and a `<label>`, so it
needs no JavaScript. The checkbox must be the `<nav>`'s preceding sibling,
which is why the switcher comes first in the DOM and `order` sets the visual
order. It is not a `<details>` because the same nav renders inline on wide
screens. `.site-menu-text` is its localised accessible name.

The footer is one line of prose, four labelled groups - Products, About Keera,
Resources, Legal - and `© 2026 bespinian · Bern`. A new page or profile goes
into one of the four groups; no fifth group, no loose link.

## Icons and logos

Nine line glyphs per language: inline `<svg class="icon">`, 24 viewBox,
`stroke="currentColor"`, `aria-hidden`. The gateway (an arrow through a gate)
and the engine (a chip) on their home card and their hero; the chat bubble on
the chat hero; cloud, rack and building on `index.html#deploy`; the leaf in the
`#partners` heading on the sustainability pages, which takes its green from the
theme. Nothing else gets an icon.

The Keera and Omnivor marks in `sustainability.html#omnivor` are a K open
around a square and an O sealed around it. The shapes must carry the contrast
alone, since red against green is the pair colour blindness flattens.

Partner wordmarks and customer logos are inline SVG with their brand fills,
`role="img"` and an `aria-label`, inside a link to the company. Their masters
are in `../artwork/`: crop the page copy to its path bounds and round to two
decimals. A dark-scheme rule turns partner paths to `--ink`. A logo, or part of
one, drawn white or black for a single ground carries `.partner--ink` or
`.customer-ink` and takes `--ink` in both schemes; nine also swaps its plate
(`.partner-plate`) and helmet (`.partner-cut`).

The provider marks on `models.html` are the gateway's `providerMarks`, filled
with `currentColor`, `aria-hidden`, beside the band's heading; marks flagged
`wide` get `.provider-mark--wide`.

The `#partners` `<h2>` is the one heading that is a direct child of `.wrap`,
so it holds a line with the leaf. Do not move another heading out to match.

## Keera's story

`story.html` tells it in four acts, one rendered comic page each, 24 panels:
I the gift (01-05), II the quiet invasion (06-12), III what it doesn't pay for
(13-17), IV the gate (18-24). The home pages carry a teaser.

- **Keera is the protagonist**, there from the first panel. **Cache**, her cat,
  is male in every language (_un chat_) and _is_ the audit trail: he stares at
  the wall in 05, and Keera builds him a ledger in 22. **Omnivor is a company**,
  never a body - only its brand, colours and buildings. _Der Konzern_ (_er_),
  _un groupe_ (_il_), _it_. The footnote saying it is invented appears on the
  story, the home teaser and the sustainability page.
- Act IV pays off earlier panels by number in its captions (19 answers 12, 21
  recalls 05, 23 recalls 16), and 24 returns to 01-02 with _Dienstagmorgen_.
  Renumbering a panel means fixing those.
- The words are drawn into the artwork, `keera-story-<lang>-page-<1-4>.webp`.
  Each act's `<figure class="comic">` carries an `<ol class="script">`
  transcript (`start` 1, 6, 13, 18) for screen readers and crawlers; `alt`
  describes the drawing, not the narration. Renders have drifted before -
  dialect, flipped panels, old product names - so check a new page against the
  transcript panel by panel.
- The setting is an unnamed small city, not Bern.
- The home teaser stays a teaser: eyebrow, a headline that introduces _her_,
  one paragraph, a quiet button, the footnote, page 1 beside it.

## The FAQs

`#faq`, a list of `<details>`, is the last section before the form on
`gateway.html` (eight questions) and `engine.html` (three), and the last
section of `chat.html` (three), nowhere else. Each
question names its product (_Does Keera Gateway add latency?_), because answer
engines quote it without the page.

The gateway's order is the argument: privacy, security and the AI Act first,
then the comparison and Claude Code, then latency, footprint and cloud-native.
The engine's: where the data goes, whether open models are good enough, how it
sits behind the gateway. The chat's: where the chats are kept, which models
it offers, what it costs - nothing beyond model usage, and no figure. Do not
soften:

- the prompt answer: content is never stored, the request is (see Positioning);
- the AI Act answer: the gateway supplies evidence, not a certificate;
- the latency answer: the microsecond figure excludes Smart Filters and Smart
  Routers, which call a small model;
- the differentiator answer: it concedes that routing is free as open source,
  names no competitor, and never calls the gateway open source;
- the open-weight answer: the large proprietary models still lead on the
  hardest reasoning; the claim is choice, not victory.

## The stylesheet

`keera.css` runs: four `@font-face` rules, the tokens, base elements,
components.

- **Tokens**: thirteen colours on `:root`, redefined - and nothing else - in one
  `prefers-color-scheme: dark` block; `@media print` restores the light values.
  `--omnivor` colours only the Omnivor mark, `--leaf` only `.theme-leaf`.
- **Contrast**: text on ground at least 5.5:1 in light and 6.7:1 in dark,
  button ink on the accent 6.5:1 / 8:1. Recheck after retuning a colour;
  `--muted`, `--accent` and `--leaf` have the least headroom.
- **Bands** alternate white and grey (`.band--alt`) down every page.
  `.card--quiet` is filled with `--surface`, so it only reads on a white band;
  `index.html#deploy` stays white and the home alternation is built around it.
- **Diagrams** are HTML and CSS so they reflow and read in order. `.sprawl`'s
  crossing paths are the one SVG, because the crossing is the argument, and the
  figure is hidden below 700px.
- **Grids** use `repeat(auto-fit, minmax(min(100%, Npx), 1fr))`; `.partners`
  alone uses `auto-fill`.
- **Breakpoints**, all of them: 1100px (the nav takes its own row), 860px (the
  flow turns into a column), 780px (splits stack), 700px (hamburger, the
  screenshot scrolls, the sprawl goes), 620px (the stack labels and
  `.facts--four` stack; the plan and model tables become one block per row).
  That restyle strips table semantics, so those tables spell out ARIA roles on
  every element.
- Inputs stay at 16px or more, or iOS Safari zooms.

## Contact form

The site's one call to action is the hero's filled _Start for free_ button
(_Kostenlos starten_, _Commencer gratuitement_) to `gateway.keera.ch` - at the
foot of the story, absent on the legal pages. The form is for everything else:
questions, comments, quotes.

It is `#contact` on the home, gateway, engine and pricing pages, posting to
Formspree (`formspree.io/f/xvkobjyb`). Formspree mails the field names as they
are, so they are localised, except `email` and `message`. Interest is a
checkbox group for the two products, the page's own one checked (the gateway on
pricing); "at least one product" is the only rule the script checks.
`contact-form.js` submits with `fetch`, reads its messages from `data-cf-*`
attributes, and calls `gtag_report_conversion()` only when Formspree accepts.

## Assets

- **`google-tag.js`** (Google Ads `AW-18327942303`) loads `defer`, last in the
  head, on every content page because an ad can land anywhere. It fetches
  gtag.js itself on `load`, after the paint; do not put a markup tag back. It
  sets the site's only cookie and has no consent gate, by decision.
- **Simple Analytics** is the last thing in the body, `async`; no cookie, no
  personal data.
- **`language.js`** loads without `defer`, ahead of the stylesheet, so the
  redirect happens before the page paints.
- **Fonts**: JetBrains Mono and Space Grotesk, variable, `latin` and
  `latin-ext`. Every head preloads the two `latin` cuts, with `crossorigin` or
  the preload is wasted.
- **Images**: masters in `../artwork/`. Encode with
  `magick <src> -resize <w>x\> -strip tmp.png && cwebp -q 82 -alpha_q 90 -m 6`;
  comic pages with `cwebp -q 82 -m 6 -sharp_yuv`, screenshots with
  `cwebp -q 92`. `width`/`height` come from the file, plus `alt` and
  `decoding="async"`; heroes get `fetchpriority="high"` and a preload as the
  first hint in the head, everything else `loading="lazy"`. `.hero-art` images
  also ship at `-400` and `-640` widths in `srcset`, with a `sizes` derived from
  the `.hero--split` grid - change the grid and every hero's `sizes` changes. The
  deploy mirrors the whole folder, so leave no unused files in it.
- **The live map screenshot** on the gateway page is a `<picture>`, dark only;
  below 700px its narrow capture is held at 700px and scrolls sideways, or the
  text would shrink to 5px. A new shot means re-reading the two paragraphs
  beside it.

## Metadata

Every content page has a `<title>`, description, canonical, `hreflang`, icons,
Open Graph tags, `twitter:card` (the only Twitter tag) and a JSON-LD `@graph`.

- Titles are written for search - what the page is and where, in the words
  people search with (LLM gateway, KI-Gateway, passerelle LLM) - and the `<h1>`
  for the reader. Keep titles under about 65 characters and descriptions
  between 100 and 160.
- The product ledes open with a definition (_Keera Gateway is a Swiss LLM
  gateway._), and headings name their subject (_How Keera Gateway works_),
  because a passage gets quoted without its page.
- Metadata URLs are absolute: `https://keera.ch/`, `/en/`, `/fr/` for the home
  pages and no `.html` elsewhere (`https://keera.ch/gateway`). Internal links
  match: `href="./"`, `href="gateway"`. Preview with `npx serve`, which resolves
  them.
- JSON-LD: `Organization` and `WebSite` on the home pages, `BreadcrumbList`
  elsewhere, `SoftwareApplication` on the product pages and pricing (offers
  only), `FAQPage` where there are FAQs. The product nodes keep one `@id` across
  languages, `https://keera.ch/#gateway` and `#engine`. The Organization's only
  `sameAs` is `linkedin.com/showcase/keera-ai`; add a profile only once it is
  real.
- Each page has its own 1200×630 Open Graph image, `keera-og-<page>.jpg`, on
  the navy of `keera-og-image.jpg`, which the home pages use. Pricing and the
  model catalogue borrow the gateway's; the legal pages borrow the home pages'.

## Root files

- **`sitemap.xml`** lists the thirty-six content URLs with alternates and a
  `<lastmod>`. Touch a page's `<lastmod>` only when its own content changes,
  not for shared header, footer or form edits. No `<changefreq>`, no
  `<priority>`, no `404.html`.
- **`llms.txt`** is Markdown: H1, blockquote, `## Overview`, `## Products`,
  `## Background`, `## Optional`. English URLs only; the legal pages, the
  other home pages and the sitemap go under Optional; the GitHub repo (with its
  licence) and the docs follow the gateway under Products.
- **`404.html`** renders under whatever path was requested, so every URL in it
  is root-absolute (`/assets/...`). It is `noindex, follow`, with no canonical,
  `hreflang`, Open Graph, JSON-LD or scripts. Its three languages sit in the
  body, DE, FR, EN, each in a `<div lang>`; the chrome stays German.
