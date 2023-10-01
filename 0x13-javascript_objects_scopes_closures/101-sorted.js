#!/usr/bin/node
/* script that imports a dictionary of occurrences by user id and
   computes a dictionary of user ids by occurrence.  */
const dict = require('./101-data.js');

const newDict = {};
const comps = dict.dict;

for (const key in comps) {
    if (newDict[comps[key]] === undefined) {
	newDict[comps[key]] = [key];
    } else {
	newDict[comps[key]].push(key);
    }
}

console.log(newDict);
