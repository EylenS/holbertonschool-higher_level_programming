$(document).ready(function () {
  jQuery.getJSON('https://swapi-api.hbtn.io/api/people/5', function (data) {
    $('DIV#character').append(data.name);
  })
});
