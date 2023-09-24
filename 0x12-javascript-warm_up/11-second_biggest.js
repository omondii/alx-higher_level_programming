#!/usr/bin/node

// searches the second biggest integer in the list of arguments.
const num = process.argv.slice(2).map(num => parseInt(num, 10));

if (num < 2) {
    console.log(0);
} else {
    const numSort = num.sort((a, b) => b - a);
    console.log(numSort[1]);
}
