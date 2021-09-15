#!/usr/bin/node

const request = require('request');
let url = 'https://swapi-api.hbtn.io/api/films/';
url = url + process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(response.body).title);
});
