#!/usr/bin/node
/**
 * Gets the contents of a webpage and stores it in a file.
 */

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  else {
    try {
      fs.writeFileSync(process.argv[3], body, 'utf-8');
    } catch (error) {
      console.log(error);
    }
  }
});
