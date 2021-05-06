#!/usr/bin/node

const a = 'No argument';
const b = 'Argument found';
const c = 'Arguments found';
const args = process.argv;

if (args[3]) {
  console.log(c);
} else if (args[2]) {
  console.log(b);
} else {
  console.log(a);
}
