#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let newIterator = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newList[newIterator] = list[i];
    newIterator += 1;
  }
  return (newList);
};
