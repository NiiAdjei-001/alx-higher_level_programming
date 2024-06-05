#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
let argc = 0;
argv.forEach(element => { argc++; });

const error_handling = function(err){
    if (err) throw err;
}

if (argc >= 4){
    // console.log(argv[2],argv[3])
    fs.writeFile(argv[2], argv[3], 'utf-8', error_handling)
}