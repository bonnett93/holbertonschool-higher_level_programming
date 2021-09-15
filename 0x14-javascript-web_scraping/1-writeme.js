#!/usr/bin/node

const myArgv = process.argv;
const filePath = myArgv[2];
const data = myArgv[3];
const fs = require('fs');

fs.writeFile(filePath, data, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
