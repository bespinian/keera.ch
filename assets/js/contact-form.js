/* Submit handler for the #contact form: posts to Formspree over fetch so the
   visitor never leaves the page. Every message comes from the data-cf-*
   attributes on the form, so one file serves all nine forms in all three
   languages. */
(function () {
  var SEL = "form[data-contact-form]";

  function say(form, key, ok) {
    var el = form.querySelector("[data-cf-status]");
    if (!el) return;
    el.textContent = form.getAttribute("data-cf-" + key) || "";
    el.className = "form-status is-shown " + (ok ? "is-ok" : "is-error");
  }

  document.addEventListener("submit", function (ev) {
    var form = ev.target;
    if (!form.matches || !form.matches(SEL)) return;
    ev.preventDefault();

    /* the one rule the browser cannot check itself */
    var group = form.querySelector("[data-cf-interest]");
    if (group && !group.querySelector("input:checked")) {
      say(form, "need-interest", false);
      var first = group.querySelector("input");
      if (first) first.focus();
      return;
    }

    var btn = form.querySelector("button[type=submit]");
    if (btn) btn.disabled = true;
    say(form, "sending", true);

    fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" },
    })
      .then(function (res) {
        if (!res.ok) throw new Error("formspree: " + res.status);
        var fields = form.querySelector("[data-cf-fields]");
        if (fields) fields.style.display = "none";
        say(form, "sent", true);
        form.reset();
        /* The lead exists once Formspree has taken it, so this is the one
           place the Google Ads conversion fires. Guarded, because the form has
           to keep working when the tag is blocked. */
        if (typeof gtag_report_conversion === "function")
          gtag_report_conversion();
      })
      .catch(function () {
        if (btn) btn.disabled = false;
        say(form, "error", false);
      });
  });
})();
