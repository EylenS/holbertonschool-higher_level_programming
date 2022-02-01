#!/usr/bin/node
/* This script let display the status code of a GET request. */
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log('code: ', response && response.statusCode);
});
