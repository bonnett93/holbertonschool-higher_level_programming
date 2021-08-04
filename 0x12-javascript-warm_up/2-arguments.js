#!/usr/bin/node

const myArgv = process.argv.slice(2);
if (myArgv.length === 0) {
  console.log('No argument');
} else if (myArgv.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
