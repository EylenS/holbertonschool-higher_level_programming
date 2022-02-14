$(document).ready(function () {
  jQuery.getJSON('https://swapi-api.hbtn.io/api/films/', function (data) {
    $(data.results).each(function (idx_tit, name_tit) {
      $('UL#list_movies').append('<li>' + name_tit.title + '</li>');
    });
  });
});
