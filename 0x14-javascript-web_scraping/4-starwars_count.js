#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let present = 0;

request(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(response.body).results;
  results.forEach(element => {
    const characters = element.characters;
    if (characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      present += 1;
    }
  });
  console.log(present);
});
