#!/usr/bin/node
const argv = process.argv;
let count = 0;
argv.forEach(() => { count += 1; });
if (count <= 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
