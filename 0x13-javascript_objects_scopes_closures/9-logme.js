#!/usr/bin/node

/* function that prints the number of arguments already printed and
   the new argument value */
exports.logMe = function (item) {
    if (this.count === undefined)
    {this.count = 0; } else {this.count++; }
    const pargs = this.count + ': ' + item;
    console.log(pargs);
};
