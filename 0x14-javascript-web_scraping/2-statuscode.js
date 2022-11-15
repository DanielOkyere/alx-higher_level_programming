#!/usr/bin/node

/**
 * Script displays the status code of GET request
 * Uses the request module
 */

const req = require('request');
const url = process.argv[2];
req.get(url).on('response', (response, error) => {
  if (error) console.log({ ...error });
  console.log('code: ' + response.statusCode);
});
