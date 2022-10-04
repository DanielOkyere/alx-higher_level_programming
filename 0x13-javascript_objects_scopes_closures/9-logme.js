#!/usr/bin/node

/**
 * Prints the number of args passed
 */
let n = 0;
exports.logMe = function (item) {
  console.log(n + ': ' + item);
  n++;
};
