#!/usr/bin/node
// Adds 2 ints passed as argumetns
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

// Add the 2 numbers
function add () {
  console.log(a + b);
}

add();
