#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  const string = count + ': ' + item;
  console.log(string);
  count += 1;
};
