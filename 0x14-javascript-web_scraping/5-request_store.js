#!/usr/bin/node
const request = require('request');
const fs = require('fs');
let url = process.argv[2];
let file = process.argv[3];
request.get(url).pipe(fs.createWriteStream(file, 'utf-8'));
