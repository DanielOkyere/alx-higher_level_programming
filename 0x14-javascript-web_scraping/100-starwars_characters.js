#!/usr/bin/node

/**
 * Prints out who is playing
 */

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req(url + id, function (error, response, body) {
  if (error) console.log(error);
  else {
    const character = JSON.parse(body).characters;
    character.forEach((element) => {
      req(element, function (err, res, content) {
        if (error) console.log(err);
        console.log(JSON.parse(content).name);
      });
    });
  }
});
