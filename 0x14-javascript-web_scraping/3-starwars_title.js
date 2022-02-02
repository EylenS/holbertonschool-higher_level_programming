#!/usr/bin/node
/* This script let prints the title of a Star Wars movie where
the episode number matches a given integer. */
const request = require('request');
const episodeN = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + episodeN, function (error, body) {
  if (error) {
    console.log(error);
  }
  const movieJSON = JSON.parse(body);
  console.log(movieJSON.title);
});
