#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const argc = argv.length;

if (argc >= 3) {
  request(argv[2], (err, res, body) => {
    if (err) throw err.message;
    console.log(`code: ${res.statusCode}`);
  });
}
