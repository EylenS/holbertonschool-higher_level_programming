#!/usr/bin/node
/* This script prints the number of movies where the character
“Wedge Antilles” is present. */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const options = {
  url,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const contentJSON = JSON.parse(body);
    // console.log(contentJSON);
    for (const i in contentJSON.characters) {
      // console.log(contentJSON.characters[i]);
      request.get(contentJSON.characters[i], function (error, response, body) {
        if (error) {
          console.log(error);
        }
        const namesJSON = JSON.parse(body).name;
        console.log(namesJSON);
      });
    }
  }
});
