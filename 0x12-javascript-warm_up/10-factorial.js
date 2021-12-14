#!/usr/bin/node
function factorialRecursion (n) {
  if (!process.argv[2] || n === 0) {
    return 1;
  }
  return n * factorialRecursion(n - 1);
}
const n = parseInt(process.argv[2]);
const factorial = factorialRecursion(n);
console.log(factorial);
