#!/usr/bin/node

/* Rectangle class with w&h constructors  */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
	  this.width = w;
	  this.height = h;
    }
  }
  /* Instance method that prints the rectangle usng the character 'X' */
  print () {
    for (let i = 0; i < this.height; i++) {
	    let row = '';
	    for (let j = 0; j < this.width; j++) {
        row += 'X';
	    }
	    console.log(row);
    }
  }
}
module.exports = Rectangle;
