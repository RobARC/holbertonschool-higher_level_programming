#!/usr/bin/node

const a = 'No argument';
const args = process.argv;

if (args[2]) {
  console.log(args[2]);
} else {
  console.log(a);
}
