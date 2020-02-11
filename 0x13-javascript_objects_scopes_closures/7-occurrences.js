#!/usr/bin/node

const nbOccurences = (list, occurence) => {
  let count = 0;
  list.forEach(element => {
    if (element === occurence) { count++; }
  });
  return count;
};

module.exports.nbOccurences = nbOccurences;
