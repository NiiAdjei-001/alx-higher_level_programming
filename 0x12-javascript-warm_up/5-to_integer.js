#!/usr/bin/node
const argv = process.argv;
const val = Number.parseInt(argv[2]);
const isNumber = Number.isInteger(val);
if (isNumber) {
  console.log(`My number: ${val}`);
} else {
  console.log('Not a number');
}
