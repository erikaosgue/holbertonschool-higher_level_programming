#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (err, response, body) => {
  if (!err) {
    const listChar = JSON.parse(body).characters;
    for (let i = 0; i < listChar.length; i++) {
      request(listChar[i], (err, response, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
