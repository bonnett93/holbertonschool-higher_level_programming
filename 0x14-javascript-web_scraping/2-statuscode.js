#!/usr/bin/node

const requestURL = process.argv[2];
const request = require('request');

request(requestURL, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
