// Side progress rail: one segment per H2 section, sized by section length. The part of a section
// currently on screen is highlighted on its segment.

const sections = [...document.querySelectorAll("main section")].filter(
  (section) => section.firstElementChild?.tagName === "H2",
);

if (sections.length > 0) {
  const rail = document.createElement("nav");
  rail.className = "progress-rail";

  const segments = sections.map((section) => {
    const segment = document.createElement("a");
    segment.className = "progress-segment";
    segment.href = `#${section.id}`;
    segment.title = section.firstElementChild.textContent;
    return segment;
  });
  rail.append(...segments);
  document.body.append(rail);

  const clamp = (x) => Math.min(Math.max(x, 0), 1);

  // The rail lines up with the title until it scrolls past the centered position.
  const title = document.querySelector(".blog-title");

  const update = () => {
    const top = title?.getBoundingClientRect().top ?? 0;
    rail.style.top = `${Math.max(innerHeight * 0.05, top)}px`;
    sections.forEach((section, i) => {
      const { top, height } = section.getBoundingClientRect();
      segments[i].style.flexGrow = height;
      segments[i].style.setProperty("--from", `${clamp(-top / height) * 100}%`);
      segments[i].style.setProperty("--to", `${clamp((innerHeight - top) / height) * 100}%`);
    });
  };

  addEventListener("scroll", update, { passive: true });
  addEventListener("resize", update);
  // images change section heights once loaded
  addEventListener("load", update);
  update();
}
