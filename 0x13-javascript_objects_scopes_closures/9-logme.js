#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
    let string = count + ': ' + item;
    console.log(string);
    count += 1;
};
