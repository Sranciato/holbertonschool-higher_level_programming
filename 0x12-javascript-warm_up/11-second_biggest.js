#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let max = 0;
  const sorted = process.argv.sort().slice(2);
  for (let i = 0; i < sorted.length; i++) {
    if (sorted[i] > max && sorted[i] < sorted[sorted.length - 1]) {
      max = sorted[i];
    }
  }
  console.log(max);
}
