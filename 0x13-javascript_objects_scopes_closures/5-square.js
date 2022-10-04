#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

/**
 * Definition of a square class which inherits from
 * Rectangle class
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
