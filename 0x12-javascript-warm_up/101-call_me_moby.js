#!/usr/bin/node
// a function that executes x times a function.
exports.callMeMobby = function (x, func) {
    for (;x > 0; x--) { func(); }
};
