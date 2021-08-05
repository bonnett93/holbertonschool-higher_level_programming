#!/usr/bin/node

const myArgv = process.argv.slice(2);

if (Number.isNaN(myArgv[0]) || myArgv.length === 1) {
  console.log(0);
} else {
  myArgv.sort(function (a, b) { return a - b; });
  console.log(myArgv[myArgv.length - 2]);
}
