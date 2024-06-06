#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const argc = argv.length;
let count = 0;

const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';

const fnx = function (err, res, body) {
  if (err) throw err.message;
  const resource = JSON.parse(body);
  const films = resource.results;
  for (const film of films) {
    const characters = film.characters;
    for (const character of characters) {
      if (character === wedgeAntilles) {
        count++;
      }
    }
  }
  console.log(count);
};

if (argc >= 3) {
  request(`${argv[2]}`, fnx);
}
