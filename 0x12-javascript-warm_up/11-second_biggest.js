#!/usr/bin/node
/**
 * Script prints the second biggest number
 * @a: List of argv
 * Return: Second biggest number
 */
if (process.argv.length > 3) {
  const args = process.argv.map(Number);
  args.slice(2);
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
} else {
  console.log(0);
}
