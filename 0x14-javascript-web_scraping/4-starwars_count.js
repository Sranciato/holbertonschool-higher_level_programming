#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const peopleUrl = 'https://swapi.co/api/people/18/';
request.get(url, function (error, response, body) {
  if (error) {
    return;
  }
  let count = 0;
  for (const movie of JSON.parse(body).results) {
    for (const people of movie.characters) {
      if (people === peopleUrl) { count++; }
    }
  }
  console.log(count);
});
