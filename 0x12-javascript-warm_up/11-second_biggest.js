#!/usr/bin/node

// searches the second biggest integer in the list of arguments.
const num = process.argv.length;
if (num <= 3) {
  console.log(0);
} else {
  const numSort = process.argv.sort();
  console.log(numSort.reverse()[1]);
}
