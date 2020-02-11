#!/usr/bin/node

module.exports.esrever = function (list) {
  const NewList = [];
  for (let x = list.length - 1; x >= 0; x--) { NewList.push(list[x]); }

  return NewList;
};
