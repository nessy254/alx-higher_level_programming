$(document).ready(function () {
  // Adds a click event listener to the <div> element with the ID "add_item"
  $('#add_item').click(function () {
    // Creates a new <li> element with the text "Item"
    const newItem = $('<li>').text('Item');

    // Appends the new <li> element to the <ul> with class "my_list"
    $('UL.my_list').append(newItem);
  });
});
