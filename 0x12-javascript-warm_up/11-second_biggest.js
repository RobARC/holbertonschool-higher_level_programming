#!/usr/bin/node

const args = process.argv;
// const a = parseInt(args[2]);
let biggest = 0;
let SecondB = 0;

if (!args || args.length <= 1) {
  console.log(0);
}
if (args.length >= 2) {
  for (let i = 0; i < args.length; i++) {
    if (parseInt(args[i]) > biggest) {
      biggest = parseInt(args[i]);
    }
  }

  for (let j = 0; j < args.length; j++) {
    if (parseInt(args[j]) < biggest && parseInt(args[j]) > SecondB) {
      SecondB = parseInt(args[j]);
    }
  }
}
console.log(SecondB);
