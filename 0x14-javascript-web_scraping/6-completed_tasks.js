#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const argc = argv.length;

if (argc >= 3) {
  const resourceURI = argv[2];
  request(resourceURI, 'json', (err, res, body) => {
    if (err) throw err.message;
    const resources = JSON.parse(body);
    // console.log(resources);
    const dict = {};
    for (const item of resources) {
      // console.log(item);
      if (item.completed === true) {
        if (dict[item.userId] !== undefined) {
          dict[item.userId] += 1;
        } else {
          dict[item.userId] = 1;
        }
      }
    }
    console.log(dict);
  });
}
