const lightbox = document.getElementById("lightbox");
const lightboxImg = document.getElementById("lightbox-img");
const lightboxTitle = document.getElementById("lightbox-title");
const lightboxFilename = document.getElementById("lightbox-filename");

document.querySelectorAll(".image-container > img").forEach((img) => {
  img.addEventListener("click", () => {
    lightboxImg.src = img.src;
    lightboxImg.alt = img.alt;

    // Extract filename from src path
    const filename = img.src.split("/").pop();
    console.log(filename);
    lightboxFilename.textContent = filename;

    // Use title attribute first, then alt text, fallback to filename
    const title = img.title || img.alt || filename;
    lightboxTitle.textContent = title;

    lightbox.classList.add("active");
  });
});

// click anywhere to close
lightbox.addEventListener("click", () => {
  lightbox.classList.remove("active");
});
