#!/usr/bin/node
/* This script let display the status code of a GET request. */
const request = require('request');
const url = process.argv[2];
const options = {
  url, method: 'GET'
};

request(options, function (error, response) {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code: ', response && response.statusCode);
});
