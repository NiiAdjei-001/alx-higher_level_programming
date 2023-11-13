#!/usr/bin/node
const argv = process.argv;
let max = Number.NEGATIVE_INFINITY;
let secondMax;
if (argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    const val = Number.parseInt(argv[i]);
    if (val > max) {
      secondMax = max;
      max = val;
    } else if (val > secondMax) {
      secondMax = val;
    }
  }
  console.log(secondMax);
}
