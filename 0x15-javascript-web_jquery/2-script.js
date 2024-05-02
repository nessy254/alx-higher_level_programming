$(document).ready(function () {
  // Adds a click event listener to the <div> element with the ID "red_header"
  $('#red_header').click(function () {
    // Updates the text color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});
