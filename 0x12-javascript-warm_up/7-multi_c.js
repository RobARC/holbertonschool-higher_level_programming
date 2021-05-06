#!/usr/bin/node
const a = 'C is fun';
const b = 'Missing number of occurrences';
const args = process.argv;

if (args[2] && Number.isInteger(parseInt(args[2]))) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log(a);
  }
} else {
  console.log(b);
}
