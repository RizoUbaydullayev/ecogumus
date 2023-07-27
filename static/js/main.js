// ============= our_product ================
let ourProductSlider = new Swiper('.our_product_slider', {
    wrapperClass: 'our_product_slider_wrap',
    slideClass: 'page',
    slidesPerView: 1,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
})

// ============= certificates ================
let certificatesSlider = new Swiper('.certificates_slider', {
    wrapperClass: 'certificates_slider_wrap',
    slideClass: 'page',
    slidesPerView: 3,
    spaceBetween: 10,
    pagination: {
        el: ".swiper-pagination",
        dynamicBullets: true,
    },
})
lightGallery(document.getElementById('animated-thumbnails-gallery'), {
    thumbnail: true,
    animateThumb: false,
    zoomFromOrigin: false,
    allowMediaOverlap: true,
    toggleThumb: true,
});

// ============= adaptive ================
function adaptive(width) {
    if (width > 1920) {

    }
    if (width <= 1920) {

    }
    if (width <= 1280) {
        certificatesSlider.params.slidesPerView = 2;
    }
    if (width <= 1024) {

    }
    if (width <= 768) {
        certificatesSlider.params.slidesPerView = 1;
    }
    if (width <= 425) {

    }
    if (width <= 320) {

    }
	certificatesSlider.update();
};

adaptive(window.innerWidth);