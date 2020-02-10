#!/usr/bin/node
exports.converter = function (base) {
  return function myConverter (number) {
    return number.toString(base);
  };
};
