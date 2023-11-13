#!/usr/bin/node
const argv = process.argv;
const val = Number.parseInt(argv[2]);
const isNumber = Number.isInteger(val);
if (isNumber) {
  if (val > 0) {
    for (let i = 0; i < val; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
