#!/usr/bin/node
let cont = 0;
module.exports.logMe = function (item)
{
  console.log("{}: {}",cont, item);
  cont++;
}
