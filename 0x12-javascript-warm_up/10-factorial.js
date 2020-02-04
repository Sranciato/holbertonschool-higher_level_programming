#!/usr/bin/node
console.log(factorial(parseInt(process.argv[2])));
function factorial (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}
