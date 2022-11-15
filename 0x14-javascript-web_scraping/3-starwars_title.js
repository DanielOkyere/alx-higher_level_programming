#!/usr/bin/node

/**
 * Script prints the title of Star Wars movie
 */

const req = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req(url, function(error, response, body){
    console.log(body)
})