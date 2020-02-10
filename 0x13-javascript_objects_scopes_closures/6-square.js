#!/usr/bin/node
const DontDoThis = require('./5-square');

class Square extends DontDoThis {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let x = 0; x < this.height; x++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
