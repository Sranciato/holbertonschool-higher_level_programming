#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2] + '/';
request.get(url, 'response', function (error, response, body) {
  if (error) {
    return;
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
