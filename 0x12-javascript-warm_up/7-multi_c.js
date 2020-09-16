#!/usr/bin/node
const result = parseInt(Number(process.argv[2]));
if (isNaN(result)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < result; i++) {
    console.log('C is fun');
  }
}
