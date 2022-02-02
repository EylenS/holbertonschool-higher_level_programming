#!/usr/bin/node
/* This script prints the number of movies where the character
“Wedge Antilles” is present. */
const request = require('request');
const url = process.argv[2];
const options = {
  url,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const resultsJSON = JSON.parse(body).results;
    let count = 0;
    for (let x = 0; x < resultsJSON.length; x++) {
      for (let y = 0; y < resultsJSON[x].characters.length; y++) {
        if (resultsJSON[x].characters[y].endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('status code:', response && response.statusCode);
  }
});
