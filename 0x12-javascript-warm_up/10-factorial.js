#!/usr/bin/node
/**
 * This code prints out the factorial
 * Using recursive method
 * @a: value to determine factorial
 * Return: factorial of number
 */
function factorial (a) {
  if (a < 0 || isNaN(a)) {
    return (1);
  } else if (a < 2) {
    return (a);
  } else {
    return (a * factorial(a - 1));
  }
}
console.log(factorial(Number(process.argv[2])));
