#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint = function (c) {
    let printCharacter = c;
    if (!printCharacter) {
      printCharacter = 'X';
    }
    let col = '';
    for (let c = 0; c < this.width; c++) {
      col += printCharacter;
    }
    for (let r = 0; r < this.height; r++) {
      console.log(col);
    }
  };
}

module.exports = Square;
