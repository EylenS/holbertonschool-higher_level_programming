#!/usr/bin/node
function add (a, b) {
  const result = a + b;
  return result;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const sum = add(a, b);
console.log(sum);
