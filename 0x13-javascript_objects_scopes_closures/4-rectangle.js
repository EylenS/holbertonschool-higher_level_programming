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

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
