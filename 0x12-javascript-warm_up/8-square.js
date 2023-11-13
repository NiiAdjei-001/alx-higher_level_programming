#!/usr/bin/node
const argv = process.argv;
const val = Number.parseInt(argv[2]);
const isNumber = Number.isInteger(val);
if (isNumber) {
  let len = '';
  if (val > 0) {
    for (let i = 0; i < val; i++) {
      len += 'X';
    }
    for (let i = 0; i < val; i++) {
      console.log(len);
    }
  }
} else {
  console.log('Missing size');
}
