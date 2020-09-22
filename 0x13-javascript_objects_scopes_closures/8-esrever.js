#!/usr/bin/node
exports.esrever = function (list) {
  const newArray = [];
  list.forEach(element => {
    newArray.unshift(element);
  });
  return (newArray);
};
