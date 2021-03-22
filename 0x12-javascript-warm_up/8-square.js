#!/usr/bin/node

let a = '';
const b = 'Missing size';
const args = process.argv;
const size = parseInt(args[2]);

if (args[2] && Number.isInteger(parseInt(args[2]))) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      a += 'X';
    }
    if (i < (size - 1)) {
      a += '\n';
    }
  }
  console.log(a);
} else {
  console.log(b);
}
