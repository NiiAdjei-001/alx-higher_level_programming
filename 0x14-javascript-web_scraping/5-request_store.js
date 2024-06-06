#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
const request = require('request');
const argc = argv.length;

if (argc >= 4) {
  const resouceUrl = argv[2];
  const outputFile = argv[3];
  request(resouceUrl, (err, res, body) => {
    if (err) throw err.message;
    fs.writeFile(outputFile, body, 'utf-8', (err) => {
      if (err) throw err.message;
    });
  });
}
