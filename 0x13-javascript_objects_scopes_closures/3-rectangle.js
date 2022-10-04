#!/usr/bin/node

/**
 * Modified class in javascript
 * If w or h is 0 an empty object is created
 */
class Rectangle {
  constructor (h, w) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      console.log('X'.repeat(this.height));
    }
  }
}

module.exports = Rectangle;
