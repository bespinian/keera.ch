/* Google's two tags, kept out of the markup like the rest of the site's
   JavaScript: the Google Ads tag (AW-18327942303) and the Google Tag Manager
   container (GTM-KLJMRV64) that runs Google Analytics. Both sit on every page,
   not only the fifteen with a form, because an ad click lands wherever the ad
   points and the click id has to be recorded there. They share one dataLayer. */
window.dataLayer = window.dataLayer || [];
function gtag() {
  dataLayer.push(arguments);
}
gtag("js", new Date());
gtag("config", "AW-18327942303");

/* gtag.js and gtm.js are fetched on `load` rather than from async <script>s in
   the head, so their third-party handshakes and payloads land after the paint
   instead of competing with the hero image. Nothing is lost: the calls above
   queue on dataLayer and both libraries replay the queue when they arrive. */
window.addEventListener("load", function () {
  [
    "https://www.googletagmanager.com/gtag/js?id=AW-18327942303",
    "https://www.googletagmanager.com/gtm.js?id=GTM-KLJMRV64",
  ].forEach(function (src) {
    var s = document.createElement("script");
    s.async = true;
    s.src = src;
    document.head.appendChild(s);
  });
});

/* Called by contact-form.js once Formspree accepts a submission. */
function gtag_report_conversion() {
  gtag("event", "conversion", {
    send_to: "AW-18327942303/snIDCLO10vYcEJ_puKNE",
  });
}
