#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('Not a number');
} else {
  const result = parseInt(process.argv[2]);
  if (result === result) {
    console.log('My number:', result);
  } else {
    console.log('Not a number');
  }
}
