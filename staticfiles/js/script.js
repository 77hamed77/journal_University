// header sticky :
// javascript for navigation bar effect on scroll
window.addEventListener("scroll", function () {
  var headere = document.querySelector("header");
  headere.classList.toggle("sticky", this.window.scrollY > 0);
});

// javascript for responsive navigation bar sidebar menu
var menu = document.querySelector(".menu");
var menuBtn = document.querySelector(".menu-btn");
var closeBtn = document.querySelector(".close-btn");
menuBtn.addEventListener("click", () => {
  menu.classList.add("active");
});
closeBtn.addEventListener("click", () => {
  menu.classList.remove("active");
});

// scroll :
const scrollRevealOption = {
  distance: "50px",
  origin: "bottom",
  duration: 1000,
};
ScrollReveal().reveal("header", {
  ...scrollRevealOption,
  // delay: 500,
  // interval: 500,
  distance: "100px",
  origin: "top",
});


// -----------slider--------------
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 30,
  freeMode: true,
  //grabCursor:true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});


// mode themes [ light , night , default]
// mode languages [ arabic , english , turkish ]