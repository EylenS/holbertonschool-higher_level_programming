#!/usr/bin/node
// Create an instance method: print(), prints the rect. using the char X
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !w || h <= 0 || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
