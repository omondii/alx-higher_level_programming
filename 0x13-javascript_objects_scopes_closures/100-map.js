#!/usr/bin/node
// a script that imports an array and computes a new array.

const list = require('./100-data.js').list;

const mapped = list.map(function (value, index){
    return value * index;
});

console.log(list);
console.log(mapped);
