#!/usr/bin/node
/* script that prints the title of a Star Wars movie where the episode number matches
a given integer. */
const request = require('request');
const argv = process.argv;
const url = 'http://swapi.co/api/films/';

request(url + argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
