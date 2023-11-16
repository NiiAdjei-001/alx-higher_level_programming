#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const fileASrc = argv[2];
const fileBSrc = argv[3];
const fileCSrc = argv[4];

fs.readFile(fileASrc, (err, data) => {
  if (err) throw err;
  fs.writeFile(fileCSrc, data.toString(), (err) => {
    if (err) throw err;
  });
});
fs.readFile(fileBSrc, (err, data) => {
  if (err) throw err;
  fs.appendFile(fileCSrc, data.toString(), (err) => {
    if (err) throw err;
  });
});
