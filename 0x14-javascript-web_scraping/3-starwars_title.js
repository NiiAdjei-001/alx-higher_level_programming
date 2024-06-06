#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const argc = argv.length;

const apiUri = 'https://swapi-api.alx-tools.com/api/films/';

const fnx = function (err, res, body) {
  if (err) throw err.message;
  const resource = JSON.parse(body);
  console.log(`${resource.title}`);
  // console.log(JSON.stringify(res));
};

if (argc >= 3) {
  request(`${apiUri}${argv[2]}`, fnx);
}
