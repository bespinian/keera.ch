/* Sends a first-time visitor on the German home page to the language their
   browser asks for: French to /fr/, anything that is not German to /en/. The
   Apache host did this with an Accept-Language rewrite, and GitHub Pages
   serves static files only, so the rule runs here instead - on the German root
   alone. Deep links and the other two home pages never negotiate, exactly as
   before.

   Loaded without `defer` and ahead of the stylesheet, so the redirect fires
   while the page is still parsing rather than after a flash of German. */
(function () {
  var path = location.pathname;
  if (path !== "/" && path !== "/index.html") return;

  /* Negotiate at most once per tab session. Without this, a visitor who picked
     DE in the switcher and later reloaded or followed a bookmark in the same
     tab - no referrer - would be sent back to /fr/ again. */
  var negotiated;
  try {
    negotiated = sessionStorage.getItem("keera-lang");
    sessionStorage.setItem("keera-lang", "1");
  } catch (e) {
    /* private mode: negotiate every time rather than never */
  }
  if (negotiated) return;

  /* Crawlers render this page in headless Chrome with no referrer, an empty
     sessionStorage and an en-US locale, so they would follow the redirect and
     index /en/ in place of the German root that hreflang and x-default name.
     They get the page as served, as they did from Apache. */
  if (
    navigator.webdriver ||
    /bot|crawl|spider|slurp|google|headless/i.test(navigator.userAgent)
  )
    return;

  /* A click from inside the site is a choice; Accept-Language is a guess. The
     switcher's DE link would otherwise be bounced straight back to /fr/. */
  if (document.referrer.indexOf(location.origin + "/") === 0) return;

  /* The first tag only, up to its separator, so the Swiss variants come along
     for free - de-CH, fr-CH, fr-FR. gsw is Swiss German, which some Android
     builds send ahead of de-CH. A browser that names no language at all stays
     German, which is what x-default points at. */
  var list = navigator.languages || [];
  var tag = (list[0] || navigator.language || "").toLowerCase();
  if (!tag) return;

  var base = tag.split(/[-_]/)[0];
  if (base === "fr") location.replace("/fr/");
  else if (base !== "de" && base !== "gsw") location.replace("/en/");
})();
