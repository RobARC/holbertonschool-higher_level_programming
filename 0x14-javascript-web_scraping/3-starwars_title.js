#!/usr/bin/node
const request = require('request');
const GET = request.get;
const num = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + num;

GET(url, (err, response, body) => {
  if (err) return (console.log(err));
  console.log(JSON.parse(body).title);
});