// Djot emits math as `<span class="math inline">\(...\)</span>` and
// `<span class="math display">\[...\]</span>`, convert them to MathML using Temml.
document.querySelectorAll("span.math").forEach((el) => {
  const display = el.classList.contains("display");
  const tex = el.textContent.trim().replace(/^\\[(\[]/, "").replace(/\\[)\]]$/, "");
  try {
    temml.render(tex, el, { displayMode: display });
  } catch (err) {
    console.error("Failed to render math:", tex, err);
  }
});
