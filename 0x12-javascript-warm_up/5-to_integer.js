#!/usr/bin/node
const result = parseInt(Number(process.argv[2]));
console.log(isNaN(result) ? 'Not a number' : `My number: ${result}`);
