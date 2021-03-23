#!/usr/bin/node

const args = process.argv;
const a = parseInt(args[2]);

function factorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
if (!args[2] || !Number.isInteger(a)) {
  console.log(1);
} else if (Number.isInteger(a)) {
  console.log(factorial(a));
}
