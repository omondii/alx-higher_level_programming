#!/usr/bin/node
// a function that executes x times a function.
exports.callMeMoby = function (x, func) {
  for (;x > 0; x--) { func(); }
};
