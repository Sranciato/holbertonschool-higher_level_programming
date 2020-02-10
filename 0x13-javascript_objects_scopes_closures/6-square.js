#!/usr/bin/node
const sq = require('./5-square.js');
module.exports = class Square extends sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let string = '';
    for (let y = 0; y < this.height; y++) {
      string = '';
      for (let x = 0; x < this.width; x++) {
        string += c;
      }
      console.log(string);
    }
  }
};
