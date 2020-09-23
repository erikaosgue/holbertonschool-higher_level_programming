#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (!err) {
    const newDict = {};
    const all = JSON.parse(body);
    all.forEach(task => {
      if (task.completed && newDict[task.userId] === undefined) {
        newDict[task.userId] = 1;
      } else if (task.completed) {
        newDict[task.userId] += 1;
      }
    });
    console.log(newDict);
  }
});
