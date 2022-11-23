#!/usr/bin/node

/**
 * Script writes as string to file
 * first argument is file path
 * second is string to write to
 * if error print error
 */

const fs = require('fs');

const filePath = process.argv[2];

try {
  fs.writeFileSync(filePath, process.argv[3], 'utf-8');
} catch (err) {
  console.log({ ...err });
}
