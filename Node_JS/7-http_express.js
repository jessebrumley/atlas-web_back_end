#!/usr/bin/env node

const express = require('express');
const countStudents = require('./3-read_file_async');
const app = express();

// Store original console.log and console.error
// this is done to display error and log to client to pass
// the task without having to edit the earlier function

const originalLog = console.log;
const originalError = console.error;

let logBuffer = '';

console.log = (message) => {
  logBuffer += message + '\n';
  originalLog(message);
};

console.error = (message) => {
  logBuffer += 'ERROR: ' + message + '\n';
  originalError(message);
};

// Route for / (root)
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route for /students
app.get('/students', async (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.write('This is the list of our students\n');

    try {
      const result = await countStudents('database.csv');
      res.end(logBuffer + result);
    } catch (error) {
      res.statusCode = 500;
      res.end(logBuffer + `Error: ${error.message}`);
    }
  });

// Listen on port 1245
app.listen(1245, () => {
  console.log('');
});

module.exports = app;
