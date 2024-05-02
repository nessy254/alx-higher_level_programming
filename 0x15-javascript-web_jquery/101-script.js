$(document).ready(function () {
  // Adds an item
  $('#add_item').click(function () {
    // Creates a new <li> element
    const newItem = $('<li>').text('Item');

    // Appends the new <li> element to the <ul> with class "my_list"
    $('ul.my_list').append(newItem);
  });

  // Removes item
  $('#remove_item').click(function () {
    // Removes the last <li> element from the <ul> with class "my_list"
    $('ul.my_list li:last-child').remove();
  });

  // Clears list
  $('#clear_list').click(function () {
    // Removes all <li> elements from the <ul> with class "my_list"
    $('ul.my_list').empty();
  });
});
