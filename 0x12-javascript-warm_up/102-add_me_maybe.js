#!/usr/bin/node
// a function that increments and calls a function.
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}

exports.addMeMaybe = addMeMaybe;
