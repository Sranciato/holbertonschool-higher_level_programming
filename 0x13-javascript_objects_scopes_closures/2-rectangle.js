#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || w === undefined) || (h <= 0 || h === undefined)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
};
