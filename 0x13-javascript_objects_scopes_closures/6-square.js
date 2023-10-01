#!/usr/bin/node

/* charPrint(c) that prints the rectangle using the character c
   class Square that defines a square and inherits from Square of 5-square.js:
*/
const Rectangle = require ('./5-square.js');

class Square extends Rectangle {
    charPrint (c) {
	if (c === undefined) {c = 'X';}
	const row = c.repeat(this.width);
	for (let i = 0; i < this.height; i++) {console.log(row); }
    }
}
module.exports = Square;
