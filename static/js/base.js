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
