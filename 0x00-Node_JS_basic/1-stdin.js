var fs=require("fs")
function pipedIn(cb) {
    fs.fstat(0, function(err, stats) {
        cb(null, stats.isFIFO())
    })
}

function pipedOut(cb) {
    fs.fstat(1, function(err, stats) {
        cb(null, stats.isFIFO())
    })
}


const { resolve } = require('path');
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });

  readline.question('Welcome to Holberton School, what is your name?\n', name => {
      console.log(`Your name is: ${name}`);
      readline.close();
  })
  readline.on('close', () => {
        pipedIn((err, x) => (x === true) ? console.log("This important software is now closing") : 'invalid')

  });

