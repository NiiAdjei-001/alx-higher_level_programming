#!/usr/bin/node
const dict = require('./101-data').dict;
const sortedDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (sortedDict[value.toString()] === undefined) {
    sortedDict[value.toString()] = [];
    sortedDict[value.toString()].push(key.toString());
  } else {
    sortedDict[value.toString()].push(key.toString());
  }
}
console.log(sortedDict);
