#!/usr/bin/node
/**
 * This program prints a message depending on the number of
 * arguments passed
 */
if (process.argv.length <= 2 || !process.argv) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
