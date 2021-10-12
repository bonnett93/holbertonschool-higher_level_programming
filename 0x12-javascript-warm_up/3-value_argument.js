#!/usr/bin/node

const myArgv = process.argv.slice(2);
if (myArgv[0]) {
  console.log(myArgv[0]);
} else {
  console.log('No argument');
}
