#!/usr/bin/node

// Accesing command line args using process.argv;
const args = process.argv;

// Print a string based on the number of entered ags
if (args.length <= 2) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
