#!/usr/bin/node

const a = 'Not a number';
const args = process.argv;

if (!args[2] || !Number.isInteger(parseInt(args[2]))) {
  console.log(a);
} else if (args[2] && Number.isInteger(args[2])) {
  console.log('My number: ' + args[2]);
} else {
  console.log('My number: ' + parseInt(args[2]));
}
