#!/usr/bin/node
// Prints the first arg passed to it
const args = process.argv;

// print the first arg passed to a function
const arg1 = args[2];
if (!arg1) {
  console.log('No argument');
} else {
  console.log(arg1);
}
