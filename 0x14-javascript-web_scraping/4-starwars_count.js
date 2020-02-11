#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    return;
  }
  let count = 0;
  for (const movie of JSON.parse(body).results) {
    for (const people of movie.characters) {
      if (people.indexOf('/18/') >= 0) { count += 1; }
    }
  }
  console.log(count);
});
