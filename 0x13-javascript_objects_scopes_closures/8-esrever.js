#!/usr/bin/node

exports.esrever = function (list) {
  const array1 = [];
  for (let i = list.length - 1; i >= 0; i--) {
    array1.push(list[i]);
  }
  return array1;
};
