#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  const data = response.body;

  fs.writeFile(fileName, data, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
