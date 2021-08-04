#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  // -- methods
  print () {
    let i;
    let row = '';
    for (i = 0; i < this.width; i++) {
      row = row + 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
