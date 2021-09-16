#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + filmId;

request(url, (err, response) => {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(response.body).characters
  for (character of characters) {
    request(character, (err, response) => {
      console.log(JSON.parse(response.body).name);
    });
  }
});
