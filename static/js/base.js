/**
 * Toast initializer
 */
$(".toast").toast("show");

/**
 * Back to top Button
 */
let topBtn = $("#top-btn");

$("#top-btn").click(function () {
  $(window).scrollTop(0);
});

$(window).scroll(function () {
  if ($(window).scrollTop() > 0) {
    topBtn.addClass("top-btn-show");
  } else {
    topBtn.removeClass("top-btn-show");
  }
});

/**
 * When user scroll an ID is added to the nav to add background-color
 */
$(window).scroll(function () {
  let navbar = $(".navbar");
  if ($(window).scrollTop() > 0) {
    navbar.addClass("nav-show");
  } else {
    navbar.removeClass("nav-show");
  }
});
