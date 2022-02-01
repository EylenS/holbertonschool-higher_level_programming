#!/usr/bin/node
/* This script let reads and prints the content of a file */
var fs = require('fs');
var content = fs.readFile(process.argv[2], 'utf-8', function(error, data){
    if(error) {
        console.log(error);
    } else {
        console.log(data);
    }
});
