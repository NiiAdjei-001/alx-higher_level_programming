#!/usr/bin/node
exports.esrever = function (list) {
  const listArray = Array.from(list);
  const reverseArray = [];

  for (let i = 0; i < listArray.length;) {
    reverseArray.push(listArray.pop());
  }
  return reverseArray;
};
