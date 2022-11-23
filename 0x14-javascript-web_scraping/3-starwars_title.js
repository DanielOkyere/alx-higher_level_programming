#!/usr/bin/node

/**
 * Script prints the title of Star Wars movie
 */

const req = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req(url, function (error, response, body) {
  if (error) console.log(error);
  else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
