// The generator puts all footnotes in a list at the end of the page. Move them next to where they
// are used instead. Both versions are created, the stylesheet shows the right one (see
// style/components/_footnotes.sass):
// - a sidenote in the empty space right of the content, when there is enough
// - otherwise a note at the end of the section the reference is in

const endnotes = document.querySelector("section[role=doc-endnotes]");

if (endnotes) {
  // The content of a note, without the backlink (and the paragraph left empty by it)
  const noteBody = (note) => {
    const copy = note.cloneNode(true);
    copy.querySelectorAll("[role=doc-backlink]").forEach((link) => link.remove());
    copy.querySelectorAll("p:empty").forEach((paragraph) => paragraph.remove());
    return copy.innerHTML;
  };

  for (const ref of document.querySelectorAll("a[role=doc-noteref]")) {
    const note = endnotes.querySelector(ref.getAttribute("href"));
    const number = `<span class="footnote-id">${ref.textContent.trim()}</span>`;
    const body = `<div>${noteBody(note)}</div>`;

    ref.classList.add("footnote-ref");
    ref.insertAdjacentHTML("afterend", `<aside class="sidenote">${number}${body}</aside>`);
    // The id moves here, so the reference jumps to it when the notes are shown inline
    (ref.closest("section") ?? document.querySelector("main")).insertAdjacentHTML(
      "beforeend",
      `<div class="footnote-inline" id="${note.id}">${number}${body}<a class="footnote-back" href="#${ref.id}">↩︎</a></div>`,
    );
  }

  endnotes.remove();
}
