#!/usr/bin/node

exports.converter = function (base) {
  return function (item) {
    return parseInt(item, 10).toString(base);
  };
};
