#!/usr/bin/node
/**
 * This code takes argument from cmd and convert
 * and print number of times `C is fun`
 */
const a = 'C is fun';
if (process.argv.length <= 2 || isNaN(Math.floor(Number(process.argv[2])))) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log(a);
}
