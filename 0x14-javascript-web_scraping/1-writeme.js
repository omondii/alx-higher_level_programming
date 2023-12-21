#!/usr/bin/node
// Writing a script to a file

const fs = require('fs');
const process = require('process');

const content = process.argv[3];
const file = process.argv[2];

fs.writeFile(file, content, 'utf8', function(err, data) {
    if (err) {
        console.log(err);
    }
});