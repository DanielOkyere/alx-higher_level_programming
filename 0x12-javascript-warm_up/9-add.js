#!/usr/bin/node
/**
 * Adds two integers
 */
function add (a, b) {
  return (Number(a) || Number(b)) ? Number(a) + Number(b) : NaN;
}

console.log(add(process.argv[2], process.argv[3]));
