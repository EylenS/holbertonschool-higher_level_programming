#!/usr/bin/node
/* This script let prints the title of a Star Wars movie where
the episode number matches a given integer. */
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
    console.log(JSON.parse(body).title);
  } else {
    console.log('status code:', response && response.statusCode);
  }
});
