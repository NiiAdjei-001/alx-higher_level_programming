#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print = function () {
    let col = '';
    for (let c = 0; c < this.width; c++) {
      col += 'X';
    }
    for (let r = 0; r < this.height; r++) {
      console.log(col);
    }
  };

  rotate = function () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  };

  double = function () {
    this.width *= 2;
    this.height *= 2;
  };
}

module.exports = Rectangle;
