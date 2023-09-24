#!/usr/bin/node

// A script that prints a square
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  let i = 0;
  let j = 0;
  let sq = '';
  while (i < x) {
    while (j < x) {
	  sq += 'X';
	  j++;
    }
    console.log(sq);
    i++;
  }
}
