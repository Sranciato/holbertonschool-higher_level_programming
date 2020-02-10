#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || w === undefined) || (h <= 0 || h === undefined)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let string = '';
    for (let y = 0; y < this.height; y++) {
      string = '';
      for (let x = 0; x < this.width; x++) {
        string += 'X';
      }
      console.log(string);
    }
  }
};
