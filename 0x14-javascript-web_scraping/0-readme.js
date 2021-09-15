#!/usr/bin/node

const fileName = process.argv.slice(2)[0];
const fs = require('fs');

fs.readFile(fileName, 'utf8', (err, jsonString) => {
  if (err) {
    console.log(err);
  }
  console.log(jsonString);
});
