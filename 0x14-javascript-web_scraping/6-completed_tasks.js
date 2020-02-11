#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) { return; }
  const dict = {};
  let count = 0;
  let prevId = 1;
  for (const user of JSON.parse(body)) {
    if (user.userId > prevId) {
      prevId = user.userId;
      count = 0;
      dict[prevId] = count;
    }
    if (user.completed === true) {
      dict[prevId] = count += 1;
    }
  }
  console.log(dict);
});
