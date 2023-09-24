#!/usr/bin/node

/* searches the second biggest integer in the list of arguments.
 'map' converts the rem args to int using parseInt. */
const num = process.argv.slice(2).map(num => parseInt(num, 10));

if (num < 2) {
  console.log(0);
} else {
  // Use a numeric comparison algo to sort the ints
  const numSort = num.sort((a, b) => b - a);
  console.log(numSort[1]);
}
