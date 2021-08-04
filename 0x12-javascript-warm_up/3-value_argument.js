#!/usr/bin/node

const myArgv = process.argv.slice(2);
if (myArgv.length === 0) {
  console.log('No argument');
} else {
  console.log(myArgv[0]);
}
