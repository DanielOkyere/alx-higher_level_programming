#!/usr/bin/node
/**
 * This program prints a message depending on the number of
 * arguments passed
 */
if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
