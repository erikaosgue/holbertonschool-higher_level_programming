#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (!err) {
    const results = JSON.parse(body).results;
    let sum = 0;
    for (const film of results) {
      sum = film.characters.find((url) => url.endsWith('/18/')) ? sum + 1 : sum;
    }
    console.log(sum);
  }
});
