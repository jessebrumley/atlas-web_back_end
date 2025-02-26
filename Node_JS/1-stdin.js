#!/usr/env/bin node

const readline = require('readline');

// set up readline interface
const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// display prompt
r1.question('Welcome to Holberton School, what is your name? ', (name) => {
// display response
  console.log(`Your name is: ${name}`);
  // when readline is closed, do this:
  r1.on('close', () => {
    console.log('This important software is now closing');
  });
  // close readline interface
  r1.close();
});
