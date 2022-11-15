#!/usr/bin/node

/**
 * prints actors in order
 */

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function helper (arr, i) {
  if (i === arr.length) return;
  request(arr[i], function (err, res, body) {
    if (err) console.error(err);
    console.log(JSON.parse(body).name);
    helper(arr, i + 1);
  });
}

request(url, function (err, response, body) {
  if (err) console.error(err);
  const chars = JSON.parse(body).characters;
  helper(chars, 0);
});
