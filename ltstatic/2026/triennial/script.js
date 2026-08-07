if ("scrollRestoration" in history) {
  history.scrollRestoration = "manual";
}

const scrollPositionKey = "ticc:scrollPosition";

function saveScrollPosition() {
  sessionStorage.setItem(
    scrollPositionKey,
    JSON.stringify({
      x: window.scrollX,
      y: window.scrollY,
      path: window.location.pathname
    })
  );
}

function restoreScrollPosition() {
  const saved = sessionStorage.getItem(scrollPositionKey);
  if (!saved) return;

  let position;
  try {
    position = JSON.parse(saved);
  } catch {
    sessionStorage.removeItem(scrollPositionKey);
    return;
  }

  sessionStorage.removeItem(scrollPositionKey);
  if (position.path !== window.location.pathname) return;

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      const root = document.documentElement;
      const previousScrollBehavior = root.style.scrollBehavior;
      root.style.scrollBehavior = "auto";
      window.scrollTo({
        left: position.x || 0,
        top: position.y || 0,
        behavior: "auto"
      });
      root.style.scrollBehavior = previousScrollBehavior;
    });
  });
}

function bindTestimonialToggle() {
  const marquee = document.querySelector("#testimonialsMarquee");
  if (!marquee) return;

  marquee.addEventListener("click", (event) => {
    const moreButton = event.target.closest(".testimonial-more");
    const lessButton = event.target.closest(".testimonial-less");
    if (!moreButton && !lessButton) return;

    const selectedCard = (moreButton || lessButton).closest(".testimonial-card");
    if (!selectedCard) return;

    if (moreButton) {
      selectedCard.classList.add("is-expanded");
      marquee.classList.add("is-paused");
      return;
    }

    selectedCard.classList.remove("is-expanded");
    marquee.classList.remove("is-paused");
  });
}

window.addEventListener("beforeunload", saveScrollPosition);

bindTestimonialToggle();
restoreScrollPosition();
