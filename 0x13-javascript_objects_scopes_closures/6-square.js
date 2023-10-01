#!/usr/bin/node
class Square extends require('./5-square.js') {
    charPrint(c) {
	if (c === undefined) {
	    this.print();
	} else {
	    for (let i = 0; i < this.width; i++) {
		let row = '';
		for (let j = 0; j < this.height; j++) {
		    row += 'C';
		}
		console.log(row);
	    }
	}
    }
}

module.exports = Square;
