#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
const argc = argv.length;

if (argc >= 4) {
  // console.log(argv[2],argv[3])
  fs.writeFile(argv[2], argv[3], 'utf-8', (err) => {
    if (err) throw err;
  });
}
