#!/usr/bin/node
/**
 * This code prints `My number: <first argument converted in integer>"
 */
const myNumber = Number(process.argv[2]) ? Number(process.argv[2]) : 'Not a number';
if (myNumber === 'Not a number') {
  console.log(myNumber);
} else {
  console.log('My number: ' + myNumber);
}
