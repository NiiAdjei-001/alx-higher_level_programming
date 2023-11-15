#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  Array.from(list).forEach((val) => {
    if (val === searchElement) { count++; }
  });
  return count;
};
