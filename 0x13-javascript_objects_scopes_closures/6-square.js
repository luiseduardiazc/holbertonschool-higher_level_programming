#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let x = 0; x < this.height; x++) {
        console.log('C'.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
