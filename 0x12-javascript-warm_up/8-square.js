#!/usr/bin/node
const result = parseInt(Number(process.argv[2]));
if (isNaN(result)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < result; i++) {
    let x = '';
    for (let j = 0; j < result; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
