/* Submit handler for the #contact form: posts to Formspree over fetch so the
   visitor never leaves the page. Every message comes from the data-cf-*
   attributes on the form, so one file serves all fifteen forms in all three
   languages. */
(() => {
  const say = (form, key, ok) => {
    const el = form.querySelector("[data-cf-status]");
    if (!el) return;
    el.textContent = form.getAttribute(`data-cf-${key}`) ?? "";
    el.className = `form-status is-shown ${ok ? "is-ok" : "is-error"}`;
  };

  document.addEventListener("submit", async (ev) => {
    const form = ev.target;
    if (!form.matches("form[data-contact-form]")) return;
    ev.preventDefault();

    /* the one rule the browser cannot check itself */
    const group = form.querySelector("[data-cf-interest]");
    if (group && !group.querySelector("input:checked")) {
      say(form, "need-interest", false);
      group.querySelector("input")?.focus();
      return;
    }

    const btn = form.querySelector("button[type=submit]");
    if (btn) btn.disabled = true;
    say(form, "sending", true);

    try {
      const res = await fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" },
      });
      if (!res.ok) throw new Error(`formspree: ${res.status}`);
    } catch {
      if (btn) btn.disabled = false;
      say(form, "error", false);
      return;
    }

    const fields = form.querySelector("[data-cf-fields]");
    if (fields) fields.hidden = true;
    say(form, "sent", true);
    /* The lead exists once Formspree has taken it, so this is the one place
       the Google Ads conversion fires. Guarded, because the form has to keep
       working when the tag is blocked. */
    if (typeof gtag_report_conversion === "function") gtag_report_conversion();
  });
})();
