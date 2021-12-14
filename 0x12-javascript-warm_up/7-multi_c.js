#!/usr/bin/node
const x = parseInt(process.argv[2]);
let i = 1;
if (parseInt(process.argv[2])) {
  if (x > 0 && x > i) {
    for (i = 1; i <= x; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
