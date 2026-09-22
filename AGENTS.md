# Keera Website

Eighteen hand-written static content pages plus `404.html`, served off GitHub
Pages with no build step. `.github/workflows/deploy.yml` publishes the repo
there on every push to `main`. The host runs no configuration of its own: what
`.htaccess` used to express is now either a Pages setting, a Pages default, or
gone - see the README.

Markup carries classes only. The whole design lives in `assets/css/keera.css`.
Four scripts run on the site: `assets/js/contact-form.js` on the nine pages
with a form, `assets/js/google-tag.js` and the hosted Simple Analytics tag on
all eighteen content pages, and `assets/js/language.js` on the German home page
alone.

Never add inline `style` attributes, per-page `<style>` blocks, or client-side
rendering. Write plain HTML with classes and put new rules in the stylesheet.

## Design rules

- **Quiet, one accent, two schemes.** One accent colour on a white or near-black
  ground, following the viewer's system setting. No gradients, no glows, no
  animation.
- **Every colour goes through a token.** A hex value outside the token block is
  a bug - it can only be right in one of the two schemes.
- **The accent is blue (`--accent`)** everywhere but the three sustainability
  pages, which carry `class="theme-leaf"` on `<body>` and run the same design in
  green. That is a swap, not an addition: no page shows both. No other page gets
  a theme class.
- **Two lines break the one-accent rule, and they are a pair:** `.sprawl-void`
  under `index.html#problem` in `--err`, and `.flow-branch` under
  `gateway.html#architecture` in `--ok`. Same slot, opposite meaning. Move them
  together, and do not add a third.
- **One idea per section.** A heading, at most two short paragraphs, and either
  three or four short cards or one table.
- **Simple language.** Short sentences, plain words. German uses _du_, English
  _you_, French _vous_.
- **One diagram and two images per product page.** A diagram has to say
  something the prose does not, or it is decoration.
- **Keera stays.** The mascot and comic artwork are the point of difference. The
  four hero cut-outs sit in a bare `.hero-art` figure: the mascot with her gun
  on the home page, Keera at her laptop on Keera Code, Keera striding through a
  gate on Keera Gateway, Keera patching a rack on Souveränität. Every other page
  leads with one illustration of its own.

Do not add: logo strips, fake terminal sessions, benefit grids, integration
cards, pricing tiers, customer quotes, hosted-provider model tables, or a
light/dark screenshot toggle.

## Pages

Keera Gateway is the more important product and comes first wherever the two are
listed: nav, footer, home cards, form checkboxes, sitemap, opening sentence.

That order is one story, and the whole site tells it: the gateway is the wedge,
because it also governs the models a customer already pays for, and Keera Code
is the next step. Nothing sells Keera as a coding agent - Keera Code is models,
an API, an inference server and a place - so the footer line, the home hero and
the home `og:image:alt` name the endpoint, never an agent.

- `index.html` - hero, the problem (`#problem`), the endpoint that answers it
  (`#solution`), the two products, three deployment options, the story teaser,
  the form. Four visuals and no more: the hero, the `.sprawl` figure, the
  `.stack`, and page 1 of the comic.

  `#problem` states the problem before naming the product. Its `<h2>` is the
  missing overview; three `.facts` cells carry the damage - no overview, no
  control of the spend, the four foreign providers everything hangs on - and the
  `.sprawl` figure closes it: three teams, six paths, nothing in the middle. The
  middle cell is about cost control, which sets up the Budgets row of
  `#solution`.

  `#solution` is the six things the endpoint does - unified API, guardrails,
  budgets, observability, routing, sovereignty - as a six-row `.stack` in the
  full `.wrap`. The shared borders are the argument: one endpoint, not six loose
  features. The first row carries `.stack-layer--api`, the row a client touches.
  These six names are independent of `gateway.html#features`; renaming a card
  there moves nothing here.

  `#problem` and `#solution` are a pair - a change to either wants a look at the
  other.

- `gateway.html` - hero, the request-flow diagram (`#architecture`), four things
  it controls (`#security`, cards only), the web UI shot, six features
  (`#features`), eight questions (`#faq`), the form. The hero is its only
  illustration.

  `#security` and `#features` are the same page at two altitudes:
  `#security` is what the endpoint decides for the business, `#features` is what
  the product is made of - guardrails, smart filters, smart routers, the live
  map, agent sandboxes, SSO and roles. It is the one six-card section on the
  site and gets no second sentence of framing. Those six names are the
  gateway's own: check the gateway repo before rewording one.

- `code.html` - hero, what it is as a four-layer stack (`#what`), the model
  table, where it plugs in beside the pair-programming illustration, four
  questions (`#faq`), the form.
- `sovereignty.html` - the layer table, three questions, what the gateway routes
  abroad and what it does not, the open-source stack. The argument is Keera
  Gateway's; Keera Code is one client of it, not the subject. `.layer-table` is
  the site's one named table: its last column - _dein Tenant_, _nur CH_,
  _Schweiz_, _Bern_ - is in the accent, because those six words are the page's
  whole argument.
- `sustainability.html` - two levers and one story: how we pick infrastructure
  partners (`#partners`), how Keera spends fewer tokens (`#tokens`), the Omnivor
  contrast, what we claim and what we do not. Swiss hosting is a fact here, not
  the argument - a mono line under `#partners` says a Swiss address alone is not
  a sustainability argument. Its hero is its only image.
- `story.html` - the comic in four acts, four rendered pages, 24 panels.

## Root files

`robots.txt`, `sitemap.xml`, `llms.txt`, `404.html` and `CNAME` sit at the
root. `CNAME` holds the single line `keera.ch` and is what binds the custom
domain to the deployment; it has to match the custom domain set under Settings
-> Pages, and removing it takes the site off that name.

The sitemap lists all eighteen content URLs with `xhtml:link` alternates and a
`<lastmod>`. Regenerate it when a page is added, and touch the `<lastmod>` of
any page whose content changed. No `<changefreq>`, no `<priority>`, and
`404.html` is not in it.

`llms.txt` is the [llmstxt.org](https://llmstxt.org/) file: an H1, a blockquote
summary, a few lines of orientation, then `## Overview`, `## Products`,
`## Background` and `## Optional`, each a list of `[title](url): description`
links. It is Markdown despite the `.txt` name. Only the six English URLs are in
it, with the German and French home pages under `## Optional`. The descriptions
are the pages' own `<meta name="description">` strings, so a reworded
description belongs in both places. Keep the products in gateway-then-code
order.

## The 404 page

GitHub Pages serves a root `404.html` for every missing path, in all three
language trees, so this one page is built differently from the eighteen:

- **Every URL in it is root-absolute** (`/assets/...`, `/code.html`, `/`),
  because it renders under the path that was requested. This is the one place
  where `../assets/...` is wrong.
- **It carries `noindex, follow`** and no canonical, `hreflang`, Open Graph or
  JSON-LD.
- **The three languages sit in the body.** No DE/FR/EN switcher; a `.facts`
  three-up under the hero carries one sentence and one home link per language,
  each in a `<div lang="...">`. The `<h1>` names all three.
- Header, footer and nav labels stay German. No form and not the home page, so
  it loads none of the four scripts, analytics included. It uses
  `keera-coding-on-a-laptop.webp`
  and adds no CSS.

## Languages

Three languages, six pages each. German (Swiss spelling - `ss`, never `ß`) is
the default at the root, English under `en/`, French under `fr/`, with the same
six filenames. Filenames stay English; only the prose is translated.

Every page carries a DE/FR/EN switcher in the header, always in that order with
the current language unlinked, and four `rel="alternate" hreflang` links in
`<head>` (`de`, `fr`, `en`, `x-default`, the last pointing at the German page).
`<html lang>` is `de-CH`, `en` or `fr`.

`assets/js/language.js` negotiates the entry point, on the German home page
only: a first language tag of `fr` is replaced with `/fr/`, `de` or `gsw` stays
German, anything else goes to `/en/`. A browser that names no language, and an
arrival referred from this site, do not redirect; neither does a second arrival
in the same session, so a click on DE in the switcher is not bounced back.
Subpages and the two other home pages never negotiate.

Apache did this server-side, and moving it into the page has one consequence
worth knowing: a crawler that executes JavaScript and reports `en-US` now
follows the redirect to `/en/`, where the header-less request the old rule saw
stayed on the German root. `x-default` still points at the German page.

Adding or editing a page means touching all three copies. Beyond the prose, only
two things differ: asset URLs are `../assets/...`, and the switcher points at
`../<page>.html` and `../<other>/<page>.html`.

French follows French punctuation spacing - a `&nbsp;` before `:`, `;`, `?` and
`!`, and inside `«&nbsp;…&nbsp;»`. **Exception:** `<meta name="description">`
and the JSON-LD share one string and a `<script>` decodes no entities, so the
French descriptions carry a literal U+00A0 instead.

Keep these French terms stable: _souveraineté_, _durabilité_, _poids ouverts_,
_codage agentique_, _dépôt_ for repository, _tenant_ untranslated, _masquage_
for redaction, _groupe_ for Omnivor, and _nLPD_ where the German says revDSG.
Every character French adds already sits in the `latin` / `latin-ext` font cuts
that ship.

`bespinian.io` has no French locale, so the French footer links to the English
`bespinian.io/en/...` imprint.

## Header and footer

The header is one flex row: wordmark, five nav links (Gateway, Code,
Sovereignty, Sustainability, the story), and the DE/FR/EN switcher. No header
CTA and no header Contact link.

It renders three ways: labels inline beside the wordmark above 1000px, on a
full-width row of their own between 700px and 1000px, and behind a hamburger
below 700px, where the switcher stays visible beside the toggle.

The toggle is a `<label>` for the visually hidden `.site-menu-state` checkbox,
so the menu needs no JavaScript. Three things are load-bearing:

- The checkbox has to be the `<nav>`'s **preceding sibling**, which is why the
  switcher sits before the nav in the DOM and the visual order comes from
  `order`. Reordering the markup breaks the sibling selector.
- It is a checkbox and **not `<details>`**: the same `<nav>` renders inline
  above the breakpoint, which a closed `<details>` cannot do.
- `.site-menu-text` is the checkbox's accessible name. It stays in the markup,
  hidden with a clip, and is localised (`Menü` / `Menu` / `Menu`).

The footer is one line of prose, one row of links (the five pages, Contact,
Imprint) and one mono line with the copyright and the inference regions.

## Icons

Six line glyphs, all inline `<svg class="icon">` on a 24 viewBox, drawn with
`stroke="currentColor"` and `aria-hidden`:

- **The two products**, in the accent: an arrow through a gate for Keera
  Gateway, a terminal prompt for Keera Code. Each appears twice per language -
  above the `<h3>` on the home product card, and above the eyebrow in that
  product's hero.
- **The three deployment options** on `index.html#deploy`, in `--muted`: a cloud
  for the shared Swiss tenant, a rack for the dedicated one, a building for
  on-premise.
- **The leaf** in the `<h2>` of `#partners` on the sustainability pages, inside
  the heading via `.icon-head`. It is a plain `.icon` and takes the page's green
  from the theme swap, so the leaf and the swap stay together.

That is eight glyphs per language, twenty-four across the site; keep the copies
identical. Nothing else gets an icon - no nav item, no other heading, no fact
cell.

The two brand marks in `#omnivor` on the sustainability pages are **not** part
of that set: `.logo--keera` and `.logo--omnivor` are filled marks on a 32
viewBox, each in its own colour (`--accent` and `--omnivor`), 26px, inside their
own `<h3>` via `.logo-head`. They are built from the same two parts - Keera's K
open with the square in its throat, the same square sealed inside Omnivor's O -
and the shapes have to carry the contrast on their own, because red against
green is the one pair a colour deficiency flattens. Never let colour be the only
thing telling the two apart.

The `#partners` `<h2>` is **the one heading on the site outside `.prose`**, as a
direct child of `.wrap`, so it and the leaf hold one line. Do not move any other
heading out to match.

## Keera's story

`story.html`, with a teaser on the home pages.

**Keera is the protagonist**, and the subject of the arc: powerless witness,
traveller, witness again, builder. She is there from the first panel, not only
at the end.

**Cache** is her sidekick, a male cat who lives in the server room, and he *is*
the audit trail: he stares at the wall in panel 05 and someone scratches his
ears; in panel 22 the staring finally has something to point at - a ledger Keera
built for him. That pairing is the story's payoff. He is male in all three
languages; the French copy says _un chat_, never _une chatte_.

**Omnivor is a company, not a character.** It has no body in any panel - it
shows up as its brand: the colours a hall or a map flips to, a logo on a screen,
a crate, the glass tower, a key on the facade. Its cast portrait is its
headquarters. German _der Konzern_ (_er/ihn/sein_), French _un groupe_
(_il/lui/son_, never _elle_), English _it/its_. Omnivor is invented, and the
mono footnote saying so appears on `story.html`, on the home teaser and in
`sustainability.html`, using the same noun.

The page runs: hero (title, two-sentence lede, the footnote, `Vier Akte · 24
Bilder` in the eyebrow), the three-portrait cast strip, the four acts, the
figure-to-function list, _what we do not claim_, and one closing CTA.

The four acts, each a `<section class="act">` with an eyebrow, a headline and a
one-sentence lede:

- **Act I - the gift** (01-05). The server room; Omnivor arrives with a free
  plugin that works; Keera watches the relief with nowhere to put herself; Cache
  stares at the cable and only Keera follows his eyes.
- **Act II - the quiet invasion** (06-12). Page 40 of the terms, over the ocean,
  the windowless hall with a Swiss cross in one rack, a web form instead of a
  room, a map that changed colour, and the price tripling on a door with no lock.
- **Act III - what it doesn't pay for** (13-17). Cheap power, Cache by the warm
  river, diesel for uptime, waste heat over dark houses, and the decision on the
  ridge.
- **Act IV - the gate** (18-24). Rebuilt from open weights and vLLM, two
  regions, the gate, Cache's ledger, the heat routed to the valley, and a return
  to the Tuesday morning of panels 01-02.

Act IV pays off earlier panels **by number, in the caption text**: 19 answers
12, 21 catches the client name from 05, 23 lights the houses dark in 16, and 24
closes the loop on 01-02. Renumbering or dropping a panel means fixing those
captions.

The 24 panels are **drawn, lettered and numbered inside four rendered comic
pages**, one per act: page 1 is panels 01-05, page 2 is 06-12, page 3 is 13-17,
page 4 is 18-24. Each act holds exactly one `<figure class="comic">`: the page
image, then a `<figcaption>` whose `<details>` opens an `<ol class="script">`
transcript. The transcript is how a screen reader and a crawler read lettering
baked into artwork, so the `<ol>` carries `start="1"`, `start="6"`, `start="13"`
and `start="18"`, and `list-style: decimal-leading-zero` reproduces the
artwork's own `01`-`24`. Keep the `<li>` text reading as a graphic novel -
concrete, in sequence, short.

The artwork is per language, at
`assets/img/keera-story-<de|fr|en>-page-<1-4>.webp`. All twelve ship. Source
dimensions vary per language, so take `width`/`height` from the file. Encode
with `cwebp -q 82 -m 6 -sharp_yuv`; below q 80 the lettering mushes. All four
are `loading="lazy"`.

Because the words live in the artwork, **a copy change is a re-render, in three
languages**, and the lettering drifts from the copy - it has produced Swiss
dialect, inverted panels, and the old `CORA GATEWAY` name. Check a new page
against the transcript panel by panel before shipping it.

The `alt` describes the page as a page - what is drawn, in sequence - because
the transcript carries the words. Do not paste the narration into `alt`.

The setting is **an unnamed small city**, not Bern. Bern in the footer is a real
company fact and stays. Hosting is Swiss without naming zones.

The home teaser stays a teaser: eyebrow, headline, one paragraph that sketches
the arc and names Omnivor, a quiet button to `story.html`, and the footnote,
beside page 1 of that language's comic in a `.split .split--portrait`. The comic
page is lazy, capped at 360px and carries no `figcaption`. Nothing else. The
headline introduces **her**, not the product - _Keera gibt es aus einem Grund_ /
_Keera exists for a reason_ / _Si Keera existe, c'est pour une raison_ - and the
paragraph opens on _she_.

`sustainability.html#omnivor` picks the thread up: the take-until-nothing-is-left
card against Keera's picked-on-renewables card, each name preceded by its brand
mark, the footnote, and a link to the story. The refusal of the climate-neutral
claim has to survive any rewrite, there and in the story's _what we do not
claim_ section.

## The two FAQs

`#faq` is the last section before the form on `gateway.html` and `code.html`,
and nowhere else. Each is a heading, one sentence of framing, then a `.faq` list
of `<details>`. The gateway asks eight, in a plain `.band` after `#features`;
Keera Code asks four, in a `.band--alt` after the pair-programming split, which
keeps that page's bands alternating down to the form.

`<details>` needs no JavaScript and keeps its native marker. The questions are
plain `<summary>` text, not headings, so the JSON-LD is what carries the Q&A to
a crawler.

Both sets are mirrored in a `FAQPage` node in the page's JSON-LD `@graph`, and
that copy is duplicated prose: regenerate it from the markup rather than
retyping it. The French node carries literal U+00A0 where the prose writes
`&nbsp;`.

### The gateway's eight

The order is the argument: privacy, security and the AI Act first, because that
is what the banking, insurance and public-sector reader is buying; the
comparison and Claude Code next, because that decides adoption; latency,
footprint and cloud-native last. Do not re-sort by how often a question is
asked.

Three answers must not be softened:

- **The prompt answer draws the line at content, not at the record.** The
  gateway keeps the request - who, when, which model, how many tokens, which
  decision - which is what `#security` and `#web-ui` sell as the audit log. What
  is never stored is the prompt and the model's answer.
- **The AI Act answer hands the compliance work back.** The gateway supplies
  evidence, not a certificate.
- **The latency answer names its own exception.** The microsecond figure is the
  path through policy, budget and log; Smart Filters and Smart Routers call a
  small model and cost more.

The differentiator answer concedes first that routing is free as open source,
then names the three things that do not come with a proxy - Swiss operation,
enterprise support with a contact in Switzerland, the Keera models behind the
endpoint - and closes on the sovereignty argument in miniature: no client or
library of its own, so the customer stays independent of us as well. Do not turn
it into a comparison against a named competitor.

### Keera Code's four

Same shape and the same JSON-LD rule, ordered for a different buyer: where the
code goes first, then the two that decide adoption, then a coda handing the
reader to the other product and the form.

Two answers are load-bearing:

- **The perimeter answer keeps the same line between content and record.** The
  code and the model's answer are not stored and nothing is trained on them; the
  request is, in the customer's own log. "Nothing is logged" would contradict
  `gateway.html`.
- **The open-weight answer concedes the benchmark.** On the hardest reasoning
  the large proprietary models are still ahead. The claim is that the customer
  keeps the choice, not that open weights win everywhere.

## Models

`#models` on `code.html` is one table - `MODELL / KONTEXT / IDEAL FÜR`, three
Keera models and the customer's own fine-tune - then one sentence naming the
upstreams (Qwen-Coder, Apertus) and the Apache-2.0 licence, then one mono
footnote.

The footnote is load-bearing: the hosted models are proprietary, run on the
provider's infrastructure rather than Swiss GPUs, are blocked by default, and a
tenant opens them per team and data class. It carries the month the lineup was
checked (September 2026) - update the stamp when the sentence changes.
`gateway.html` names the same provider in the models column of its flow, so the
two pages move together.

## Gateway web UI screenshot

`#web-ui` sits between `#security` and `#features`: a heading, two paragraphs
written off the pixels, the shot in a bordered `figure.figure--shot`, and a mono
caption. The first paragraph is control - web UI and CLI writing the same
versioned policy - and the second is visibility: tokens, cost and refused
requests per team, model and period, in the browser or as CSV. That second
paragraph is the page's only observability claim and stays. The caption says the
figures come from a demo instance.

Only the dark shot ships (`keera-gateway-sessions-dark.webp`, 1920×952). Below
700px the frame scrolls sideways rather than shrinking. A replacement wants the
window artefacts cleaned off the master, a resize to 1920 wide, `cwebp -q 92`
(small UI type, not illustration), and its own `width`/`height` read off the
encoded file - and a re-read of both paragraphs.

## Contact form

Nine pages carry the same form - `#contact` on the home page and the two product
pages, in each language. It posts to Formspree
(`https://formspree.io/f/xvkobjyb`): name, e-mail, company, a checkbox group for
the two products, a free-text message, the `_subject` and `_gotcha` fields
Formspree reads itself, and a hidden field naming the language.

Formspree puts field names straight into the notification mail, so they are
localised: `Sprache`/`Language`/`Langue`, `Name`/`Unternehmen`/`Interesse`,
`Name`/`Company`/`Interest`, `Nom`/`Entreprise`/`Intérêt`. `email` and `message`
stay lowercase English. Interest is a checkbox group, not radios, so one visitor
can ask about both products; on `code.html` and `gateway.html` the page's own
product is `checked` and can be unticked.

`assets/js/contact-form.js` takes the submit over: delegated off `document`,
posts with `fetch` so the visitor never leaves the page, then hides
`[data-cf-fields]` and prints the confirmation into `[data-cf-status]`. All four
messages come from `data-cf-*` attributes on the `<form>`, so one file serves all
nine pages. A response Formspree accepts is the moment the lead exists, so that
branch - and nothing else - calls `gtag_report_conversion()`. "At least one
product" is the only rule the handler checks; everything else is native
constraint validation.

## The stylesheet

`assets/css/keera.css`, in this order: four `@font-face` rules, the tokens, the
base elements, then the components. Read it before adding a class - most
sections need nothing new.

- **Tokens** on `:root`: thirteen colours - `--bg`, `--surface`, `--card`,
  `--ink`, `--muted`, `--line`, `--accent`, `--accent-hover`, `--btn-ink`,
  `--ok`, `--err`, `--omnivor`, `--leaf` - plus two font stacks, `--wrap`
  (1040px), `--prose` (34rem) and `--radius`. `--omnivor` colours nothing but
  the Omnivor brand mark and `--leaf` nothing but the `.theme-leaf` block;
  nothing else may read either.
- **The green theme**: `.theme-leaf` sits under the dark-scheme block and is two
  rules - `--accent: var(--leaf)` plus an `--accent-hover`, and a dark-scheme
  copy of the hover. Custom properties inherit, so a declaration on `<body>`
  beats `:root` for the whole subtree.
- **Dark scheme**: one `@media (prefers-color-scheme: dark)` block redefining
  those thirteen colours and nothing else. It follows the system setting; there
  is no toggle. `:root` carries `color-scheme: light dark`. `@media print` puts
  the light values back.
- **Contrast**: every text-on-ground pair is at least 5.5:1 in light and 6.7:1
  in dark; button ink on `--accent` is 6.5:1 / 8:1. Recheck if you retune a
  colour - `--muted` and `--accent` have the least headroom.
- **Layout**: `.wrap` centres and pads a band, `.prose` caps a text column at
  34rem, `.band` is a section with a hairline top border, `.band--alt` adds the
  grey ground. Bands alternate white and grey down the page.
- **Type**: `h1`/`h2` scale with `clamp()`, `.lede` is the 19px intro,
  `.eyebrow` the small mono label above a heading, `.note` the small mono
  footnote, `.mono` for inline code-ish words.
- **Diagrams**: `.flow` is the gateway's request path - three `.flow-stage`
  boxes chained by two `.flow-arrow`s, the middle `--main` in the accent with an
  ordered `.flow-steps` list, and `.flow-branch` hanging under it in `--ok`.
  `.stack` is labelled rows sharing their borders inside one rounded block, each
  a `.stack-label` beside a `.stack-text`, with `.stack-layer--api` carrying an
  inset accent bar; it sits in a `.stack-fig` figure. Rows are parallel, not
  sequential. `.sprawl` is two `.sprawl-side` columns of `.sprawl-node` boxes
  with six SVG paths crossing between them and a `.sprawl-void` line under the
  middle in `--err`; `grid-auto-rows: 1fr` on both sides keeps the path ends on
  the node rows.

  Those paths are **the one SVG among the diagrams**: crossing diagonals are
  what HTML boxes cannot draw. Reach for SVG only when the shape itself is the
  argument. `.sprawl` is also the one diagram that does not survive a phone -
  below 700px the whole `<figure>` is `display: none`.

  The other diagrams are HTML and CSS, so they reflow from a row into a column
  (the flow at 860px with its arrows rotated, the stack's label column at 620px)
  and stay in source order for a screen reader. Arrows are `aria-hidden`.

- **`.split`**: text beside an illustration, one band down from the hero.
  Collapses to one column at 780px. `.split--portrait` caps the figure at 360px
  and centres it.
- **`.icon`**: the 30px glyph, coloured from `--accent`.
- **`.card--quiet`**: a borderless card on a `--surface` tint with a `--muted`
  icon, for the deployment options. Its fill *is* `--surface`, so it only reads
  as a card on a plain white `.band` - `index.html#deploy` therefore keeps a
  white band, and the home page's alternation is laid out around that fixed
  point.
- **Blocks**: `.grid` (auto-fit cards, `.grid--two` for the two product cards),
  `.card`, `.facts` (borderless three-up, `.facts--four` goes two-up),
  `.plain-list`, `.table-wrap` + plain `<table>` (`td.tight` keeps a short value
  on one line; `.layer-table` colours its last column in the accent by
  `:last-child`, and `code.html`'s model table stays plain), `.figure`, `.faq`,
  `.hero` / `.hero--split` / `.hero-art`, `.btn` / `.btn--quiet` / `.btn-row` /
  `.arrow`, the form controls (`.form`, `.field`, `.label`, `.input`,
  `.choices`, `.choice`, `.form-actions`, `.form-status` with `.is-shown` /
  `.is-ok` / `.is-error`, `.hp`), and the story's `.act`, `.comic`, `.script`,
  `.cast`.
- **Grids** are written `repeat(auto-fit, minmax(min(100%, Npx), 1fr))`: the
  `min(100%, …)` lets a track collapse below `N` instead of overflowing.
- **Breakpoints**, all of them: 1000px (nav takes its own row), 780px (a split
  hero stacks), 700px (nav becomes the hamburger, the screenshot scrolls, the
  sprawl figure goes), 620px (the stack's label column stacks). Plus
  `pointer: coarse`, a `print` block, and `prefers-reduced-motion`.

Text stays at or above 16px in inputs - iOS Safari zooms the page in below that.

## Assets

- `assets/css/keera.css` - the stylesheet. One file, no imports.
- `assets/js/contact-form.js` - the form handler, loaded `defer` by the nine
  pages with a form.
- `assets/js/google-tag.js` - the Google Ads tag `AW-18327942303`: the
  `dataLayer` bootstrap, the `config` call, and the conversion helper. Loaded
  `defer` by all eighteen content pages, last in the head. It sits on every page
  because an ad click lands wherever the ad points. **The file fetches gtag.js
  itself, on `load`**, so the ~120 KB third-party fetch lands after the paint;
  do not put a markup tag back. It is the site's only cookie, and it has no
  consent gate by decision.
- **Simple Analytics** - `https://scripts.simpleanalyticscdn.com/latest.js`,
  the one third-party script that is not a local file, because the vendor
  serves it. It is the last thing in the body on all eighteen content pages,
  `async` and unannotated. It sets no cookie and collects no personal data, so
  it needs no consent gate either. Not on `404.html`.
- `assets/js/language.js` - the Accept-Language redirect described under
  **Languages**. `index.html` alone loads it, and **without `defer` and ahead of
  the stylesheet**, because it has to run before the page paints; a deferred
  copy would show a flash of German first. Those three files plus the Simple
  Analytics tag are all the JavaScript the site runs.
- `assets/fonts/` - JetBrains Mono and Space Grotesk woff2 subsets, `latin` and
  `latin-ext` only, both variable-weight, so four `@font-face` rules cover the
  whole `font-weight: 400 700` range. Every head preloads the two `latin` cuts
  (`<link rel="preload" as="font" type="font/woff2" crossorigin>`, after the
  hero image preload and before the stylesheet). `crossorigin` is required even
  same-origin, or the preload is thrown away. The `latin-ext` cuts are
  deliberately not preloaded - umlauts and accents sit inside `latin`. Re-add a
  Google Fonts cut only if a page ever contains a glyph in its range.
- `assets/img/` - artwork and icons, `.webp` only; the masters live in
  `artwork/` outside this repo. Re-encoding means re-exporting the source, then
  `magick <src> -resize <w>x\> -strip tmp.png && cwebp -q 82 -alpha_q 90 -m 6`.
  `keera-og-image.jpg` is the 1200×630 social card and
  `keera-apple-touch-icon.png` the 180×180 iOS icon. Every rendition in the
  folder is referenced by a page - the deploy mirrors the whole folder, so do
  not leave spares behind.

  Artwork is plain `<img>` everywhere: `width`/`height` from the file's own
  pixel size, `alt`, `decoding="async"`, and either `loading="lazy"` or, for
  heroes, `fetchpriority="high"`. Crop and corners come from the stylesheet.
  **Every head preloads its own hero image** (`<link rel="preload" as="image"
  fetchpriority="high">`) as the first hint in the head, ahead of the fonts. The
  preload `href` must match the `<img src>` exactly, or the image downloads
  twice - a page that changes its hero changes both.

## Metadata

Every content page carries its `<title>`, `description`, `rel="canonical"`,
`hreflang` alternates, icons, Open Graph and Twitter tags and a JSON-LD block in
`<head>`. `404.html` is the exception.

Every URL in the metadata is absolute `https://keera.ch/...`, so all of them
need updating if the domain changes. Canonicals, `og:url` and the sitemap use
the directory form for the three home pages - `https://keera.ch/`, `/en/`,
`/fr/`. Internal links match: `href="./"` for the current language's home page.

The JSON-LD is one `@graph` per page: `Organization` + `WebSite` on the home
pages, `BreadcrumbList` on the subpages, plus `SoftwareApplication` and
`FAQPage` on `code.html` and `gateway.html`.

Keera has no social or directory profiles, so its `Organization` carries no
`sameAs`; `parentOrganization` points at bespinian's. Give Keera its own
`sameAs` the moment it has a real, verified profile.

Every page carries its own Open Graph image, 1200×630, built from that page's
artwork on the `#091023` navy of `keera-og-image.jpg`. The home pages keep
`keera-og-image.jpg`; the rest use `keera-og-<page>.jpg`. `og:image:alt`
describes the artwork in the page's own language.
