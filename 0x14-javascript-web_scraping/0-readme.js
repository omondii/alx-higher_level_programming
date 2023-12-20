#!/usr/bin/node
// Reading from a file using js
// fs - file System

const fs = require('fs');
const process = require('process');

const filepath = process.argv[2];
fs.readFile(filepath, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
