#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const array = process.argv.map(Number).slice(2, process.argv.length).sort(function (a, b) { return a - b; });
  console.log(array[array.length - 2]);
}
