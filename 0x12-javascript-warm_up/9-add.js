#!/usr/bin/node
console.log(add(process.argv[2], process.argv[3]));
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
