#!/usr/bin/node
/* This script gets the contents of a webpage and stores it in a file. */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
const options = {
  url,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(file, body, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
