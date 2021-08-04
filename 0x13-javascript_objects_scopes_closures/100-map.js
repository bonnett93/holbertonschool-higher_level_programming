#!/usr/bin/node

const array1 = require('./100-data').list;
const array2 = array1.map((x, y) => x * y);

console.log(array1);
console.log(array2);
