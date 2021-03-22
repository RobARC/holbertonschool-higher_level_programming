#!/usr/bin/node
const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);

function add (a, b) {
  return a + b;
}
if (!args[2] || !args[3] || !Number.isInteger(a) || !Number.isInteger(b)) {
  console.log('NaN');
}
if ((args[2] && args[3]) || (Number.isInteger(a) && Number.isInteger(b))) {
  console.log(add(a, b));
}
