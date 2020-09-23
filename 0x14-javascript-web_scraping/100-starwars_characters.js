#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (err, response, body) => {
  if (!err) {
    const film = JSON.parse(body);
    film.characters.forEach(character => {
      request.get(character, (err, response, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
