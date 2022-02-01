#!/usr/bin/node
/* This script let reads and prints the content of a file */
const fs = require('fs');
const content = process.argv[2];
fs.readFile(content, 'utf-8', function(error, data) {
    if (error) {
        console.log(error);
    } else {
        console.log(data);
    }
});
