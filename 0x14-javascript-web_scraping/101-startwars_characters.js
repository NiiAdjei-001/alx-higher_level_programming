#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const { promisify } = require('util');
const argc = argv.length;
const apiURI = 'https://swapi-api.alx-tools.com/api/films/';

const requestPromise = promisify(request);

async function runRequest () {
  try {
    const filmCharRes = await requestPromise(`${apiURI}${argv[2]}`);
    const characters = JSON.parse(filmCharRes.body).characters;

    for (const character of characters) {
      const charRes = await requestPromise(character);
      const value = JSON.parse(charRes.body).name;
      console.log(value);
    }
  } catch (error) {
    console.error(error.message);
  }
}

if (argc >= 3) {
  runRequest();
}
