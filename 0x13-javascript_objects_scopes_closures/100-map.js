#!/usr/bin/node
const oldList = require('./100-data').list;
const newArray = oldList.map(function (value, index) {
  return value * index;
});
console.log(oldList);
console.log(newArray);
