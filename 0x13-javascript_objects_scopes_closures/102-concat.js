#!/usr/bin/node
const fileC = process.argv[4];
const fs = require('fs');
const fileA = fs.readFileSync(process.argv[2], 'utf-8');
const fileB = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(fileC, fileA + fileB);
