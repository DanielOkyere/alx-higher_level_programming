#!/usr/bin/node

/**
 * Square based on 5-Square
 */
class Square extends require('./5-square.js') {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
