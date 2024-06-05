#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
let argc = 0;
argv.forEach(element => { argc++; });

const exec = function(err, data){
    if (err) throw err;
    console.log (data);
}

if (argc >= 3){
    fs.readFile(argv[2], 'utf-8', exec)
}
