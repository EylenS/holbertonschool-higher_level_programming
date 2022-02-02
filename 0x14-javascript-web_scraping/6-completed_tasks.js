#!/usr/bin/node
/* This script computes the number of tasks completed by user id
print users with completed task */
const request = require('request');
const url = process.argv[2];
const options = {
  url,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const content = JSON.parse(body);
  const dict = {};
  for (const i in content) {
    if (content[i].completed === true) {
      if (dict[content[i].userId] === undefined) {
        dict[content[i].userId] = 1;
      } else {
        dict[content[i].userId]++;
      }
    }
  }
  console.log(dict);
});
