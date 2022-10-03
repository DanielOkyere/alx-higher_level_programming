#!/usr/bin/node
/**
 * This code prints out as square provides as argv
 */
const letter = 'X';
if (process.argv.length <= 2 || isNaN(Math.floor(Number(process.argv[2])))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(letter.repeat(process.argv[2]));
  }
}
