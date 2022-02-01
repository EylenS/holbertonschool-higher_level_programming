#!/usr/bin/node
/* This script let writes a string to a file. */
const fs = require('fs');
const path = process.argv[2];
const string = process.argv[3];
fs.writeFile(path, string, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  }
});
