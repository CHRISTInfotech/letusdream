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
  const modal = document.getElementById("testimonialModal");
  const marquee = document.getElementById("testimonialMarquee");
  if (!modal || !marquee) return;

  modal.addEventListener("show.bs.modal", () => {
    marquee.classList.add("is-paused");
  });

  modal.addEventListener("hidden.bs.modal", () => {
    const selectedCard = marquee.querySelector(".is-expanded");
    if (!selectedCard) {
      marquee.classList.remove("is-paused");
      return;
    }

    selectedCard.classList.remove("is-expanded");
    marquee.classList.remove("is-paused");
  });
}

window.addEventListener("beforeunload", saveScrollPosition);

bindTestimonialToggle();
restoreScrollPosition();


/* Sticky Conference Subnav Handler & Dynamic Scrollspy */
function initStickySubnav() {
  const wrapper = document.querySelector(".conference-subnav-wrapper");
  const subnav = document.querySelector(".conference-subnav");
  const mainNav = document.querySelector(".conference-nav");
  if (!wrapper || !subnav) return;

  const links = subnav.querySelectorAll('a[href^="#"]');
  const sections = [];

  links.forEach((link) => {
    const targetId = link.getAttribute("href");
    if (!targetId || targetId === "#") return;
    const targetEl = document.querySelector(targetId);
    if (targetEl) {
      sections.push({ id: targetId, el: targetEl, link: link });
    }
  });

  function updateSticky() {
    const navHeight = mainNav ? mainNav.offsetHeight : 86;
    const wrapperRect = wrapper.getBoundingClientRect();

    if (wrapperRect.top <= navHeight) {
      if (!subnav.classList.contains("is-sticky")) {
        wrapper.style.minHeight = subnav.offsetHeight + "px";
        subnav.classList.add("is-sticky");
      }
      subnav.style.top = navHeight + "px";
    } else {
      if (subnav.classList.contains("is-sticky")) {
        subnav.classList.remove("is-sticky");
        subnav.style.top = "";
        wrapper.style.minHeight = "";
      }
    }
  }

  function updateActiveSection() {
    const navHeight = mainNav ? mainNav.offsetHeight : 86;
    const subnavHeight = subnav.offsetHeight || 50;
    const threshold = navHeight + subnavHeight + 40;
    const scrollPos = window.scrollY + threshold;

    let activeItem = null;

    // Check which section is in view
    for (let i = 0; i < sections.length; i++) {
      const s = sections[i];
      const top = s.el.offsetTop;
      const height = s.el.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        activeItem = s;
        break;
      }
    }

    // Edge case: if reached near the very bottom of the document
    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 50) {
      if (sections.length > 0) {
        activeItem = sections[sections.length - 1];
      }
    }

    // If above the first section (e.g. in the hero banner), nothing is active
    if (sections.length > 0 && scrollPos < sections[0].el.offsetTop) {
      activeItem = null;
    }

    sections.forEach((s) => {
      if (activeItem && s.id === activeItem.id) {
        if (!s.link.classList.contains("active")) {
          s.link.classList.add("active");
          // Ensure active pill is scrolled into view horizontally on smaller viewports
          const scrollContainer = subnav.querySelector(".conference-subnav-scroll");
          if (scrollContainer) {
            const linkRect = s.link.getBoundingClientRect();
            const containerRect = scrollContainer.getBoundingClientRect();
            if (linkRect.left < containerRect.left || linkRect.right > containerRect.right) {
              s.link.scrollIntoView({ behavior: "smooth", inline: "nearest", block: "nearest" });
            }
          }
        }
      } else {
        s.link.classList.remove("active");
      }
    });
  }

  // Smooth scroll offset adjustment for fixed navbar + subnav
  links.forEach((link) => {
    link.addEventListener("click", (e) => {
      const targetId = link.getAttribute("href");
      if (!targetId || targetId === "#") return;
      const targetEl = document.querySelector(targetId);
      if (!targetEl) return;
      e.preventDefault();

      // Immediate visual feedback on click
      sections.forEach((s) => s.link.classList.remove("active"));
      link.classList.add("active");

      const navHeight = mainNav ? mainNav.offsetHeight : 86;
      const subnavHeight = subnav.offsetHeight || 50;
      const targetTop = targetEl.getBoundingClientRect().top + window.scrollY - navHeight - subnavHeight + 2;
      window.scrollTo({
        top: Math.max(0, targetTop),
        behavior: "smooth",
      });
    });
  });

  function onScroll() {
    updateSticky();
    updateActiveSection();
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  updateSticky();
  updateActiveSection();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initStickySubnav);
} else {
  initStickySubnav();
}
