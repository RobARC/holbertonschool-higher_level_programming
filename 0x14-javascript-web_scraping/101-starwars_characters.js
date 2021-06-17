#!/usr/bin/node
const request = require('request');
const num = process.argv[2];
const url =  'https://swapi-api.hbtn.io/api/films/' + num;

request.get(url, function(err, res, body){
    if (err) return (console.log(err));
    const characters = JSON.parse(body).characters;

    let i = 0;
    while(i < characters.length){
        request.get(characters[i], (err, res, body) => {
            if (err){
                console.log(err);
            } else {
                const name = JSON.parse(body).name;
                console.log(name);
            }
        });
        i++;
    }
});