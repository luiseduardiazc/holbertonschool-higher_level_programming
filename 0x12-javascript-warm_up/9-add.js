#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const args = process.argv;
const num1 = parseInt(args[2], 10);
const num2 = parseInt(args[3], 10);

console.log(add(num1, num2));