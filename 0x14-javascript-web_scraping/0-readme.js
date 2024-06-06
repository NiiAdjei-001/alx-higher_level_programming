#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
const argc = argv.length;

const exec = function (err, data) {
  if (err) throw err;
  console.log(data);
};

if (argc >= 3) {
  fs.readFile(argv[2], 'utf-8', exec);
}
