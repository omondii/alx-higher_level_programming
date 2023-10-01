#!/usr/bin/node
// a function that converts a number from base 10 to another base

exports.converter = function (base) {
    return function (x) {
	return x.toString(base);
    };
};
