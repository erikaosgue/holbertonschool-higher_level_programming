#!/usr/bin/node
exports.logMe = function (item) {
  const newList = [];
  newList.push(item);
  for (let i = 0; i < newList.length; i++) {
    console.log(i + ': ' + newList[i]);
  }
};
