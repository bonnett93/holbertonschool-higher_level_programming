#!/usr/bin/node

const myArgv = process.argv.slice(2);
const myNumber = parseInt(myArgv[0]);

if (Number.isNaN(myNumber)) {
  console.log('Not a number');
} else {
  console.log('My number:', myNumber);
}
