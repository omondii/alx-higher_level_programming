#!/usr/bin/mode
exports.callMeMobby = function (x, func) {
    for (; x > 0; x--) { func(); }
};
