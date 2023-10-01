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
  rotate() {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
  }
  double(){
      if (this.width && this.height) {
	  this.width *= 2;
	  this.height *= 2;
      }
  }
}
module.exports = Rectangle;
