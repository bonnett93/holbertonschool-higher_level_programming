#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

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
}

module.exports = Rectangle;
