#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) { throw error; }
  const dict = {};
  let count = 0;
  for (const user of JSON.parse(body)) {
    if (user.completed === true) {
      if (dict[user.userId] === undefined) {
        count = 0;
        dict[user.userId] = count;
      }
      dict[user.userId] = count += 1;
    }
  }
  console.log(dict);
});
