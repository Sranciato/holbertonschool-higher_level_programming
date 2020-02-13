$(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data) {
    for (const film of data.results) {
      $('#list_movies').append($('<li></li>').text(film.title));
    }
  });
});
