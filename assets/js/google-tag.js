/* The Google Ads tag (AW-18327942303), kept out of the markup like the rest of
   the site's JavaScript. It sits on every page, not only the nine with a form,
   because an ad click lands wherever the ad points and the click id has to be
   recorded there. */
window.dataLayer = window.dataLayer || [];
function gtag() {
  dataLayer.push(arguments);
}
gtag("js", new Date());
gtag("config", "AW-18327942303");

/* gtag.js is fetched on `load` rather than from an async <script> in the head,
   so its third-party handshake and ~120 KB land after the paint instead of
   competing with the hero image. Nothing is lost: the calls above queue on
   dataLayer and gtag.js replays the queue when it arrives. */
window.addEventListener("load", function () {
  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=AW-18327942303";
  document.head.appendChild(s);
});

/* Called by contact-form.js once Formspree accepts a submission. */
function gtag_report_conversion() {
  gtag("event", "conversion", {
    send_to: "AW-18327942303/snIDCLO10vYcEJ_puKNE",
  });
}
