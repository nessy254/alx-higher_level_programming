$(document).ready(function () {
  // Fetches character data from the URL
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extracts the character name from the fetched data
    const charName = data.name;

    // Displays the character name in the <div> element with the ID "character"
    $('#character').text(charName);
  });
});
