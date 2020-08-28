/**
 * Updated bag quatity on click
 */
$(".update-link").click(function (e) {
  let form = $(this).prev(".update-form");
  form.submit();
});

/**
 * Remove item from bag and reload on click
 */
$(".remove-item").click(function (e) {
  let csrfToken = "{{ csrf_token }}";
  let itemId = $(this).attr("id").split("remove_")[1];
  let colour = $(this).data("product_colour");
  let url = `/bag/remove/${itemId}/`;
  let data = { 'csrfmiddlewaretoken': csrfToken, 'product_colour': colour };

  $.post(url, data).done(function () {
    location.reload();
  });
});
