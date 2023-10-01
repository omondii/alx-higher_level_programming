#!/usr/bin/node
exports.callMeMobby = function (x, func) {
    for (; x > 0; x--) { func(); }
};
