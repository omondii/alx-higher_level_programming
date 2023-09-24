#!/usr/bin/node

// A script that prints a square
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
    console.log('Missing size');
} else {
    let i = 0; // Var to iterate over rows
    let j = 0;// var to iterate over columns
    let row = '';
    while (i < x) {
	while (j < x) {
	    row += 'x';
	    j++;
	}
	console.log(row);
	i++;
    }
}
