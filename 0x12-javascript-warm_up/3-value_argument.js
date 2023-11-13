#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
argv.forEach(() => { count += 1; });
if (count <= 1) {
  console.log('No argument');
} else {
  console.log(argv[1]);
}
