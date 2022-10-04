#!/usr/bin/node

/**
 * Converter
 */
exports.converter = function (base) {
  function conv (num) {
    return num.toString(base);
  }
  return conv;
};
