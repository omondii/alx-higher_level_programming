#!/usr/bin/node
// Write a function that returns the reversed version of a list:

exports.esrever = function (list) {
  const newList = [];
  // traverse list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
