#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 & h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.height *= this.height;
    this.width *= this.width;
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }
}
module.exports = Rectangle;
