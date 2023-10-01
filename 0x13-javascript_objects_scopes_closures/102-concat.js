#!/usr/bin/node
// a script that concats 2 files
const fs = require('fs');
const f1 = process.argv[2];
const f2 = process.argv[3];

const content1 = fs.readFileSync(f1, 'utf-8');
const content2 = fs.readFileSync(f2, 'utf-8');

const newCont = content1 + content2;

fs.writeFile(process.argv[4], newCont, 'utf-8', (err) => {
    if (err) {
	throw err;
    }
});
