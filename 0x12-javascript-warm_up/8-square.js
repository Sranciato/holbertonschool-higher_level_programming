#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  let string = '';
  for (let y = 0; y < process.argv[2]; y++) {
    string = '';
    for (let x = 0; x < process.argv[2]; x++) {
      string += 'X';
    }
    console.log(string);
  }
}
