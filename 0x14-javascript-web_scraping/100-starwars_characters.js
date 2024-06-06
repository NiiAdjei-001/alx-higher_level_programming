#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const argc = argv.length;
const apiURI = 'https://swapi-api.alx-tools.com/api/films/';

if (argc >= 3) {
  request(`${apiURI}${argv[2]}`, (err, res, body) => {
    if (err) throw err.message;
    const characters = JSON.parse(body).characters;

    for (const character of characters) {
      request(character, (err, res, body) => {
        if (err) throw err.message;
        console.log(JSON.parse(body).name);
      });
    }
  });
}
