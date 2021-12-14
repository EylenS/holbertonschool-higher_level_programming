#!/usr/bin/node
// Define a class called Rectangle, INitializing 2 attr.
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !w || h <= 0 || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
