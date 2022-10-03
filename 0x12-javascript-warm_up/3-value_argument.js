#!/usr/bin/node
/**
 * This code prints out the value of my argument
 */
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
