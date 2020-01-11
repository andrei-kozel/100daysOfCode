let slides = document.querySelectorAll(".carousel__photo");
let prev_button = document.querySelector(".carousel__button--prev");
let next_button = document.querySelector(".carousel__button--next");
let slide = 0;

function nextSlide() {
  slides[slide].classList.remove("initial");
  if (slide === slides.length - 1) {
    slide = 0;
  } else {
    slide = slide + 1;
  }
  slides[slide].classList.add("initial");
}

function prevSlide() {
  slides[slide].classList.remove("initial");
  if (slide === 0) {
    slide = slides.length - 1;
  } else {
    slide = slide - 1;
  }
  slides[slide].classList.add("initial");
}

next_button.addEventListener("click", nextSlide);
prev_button.addEventListener("click", prevSlide);
