#!/usr/bin/env node

const http = require('http');

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!\n');
});

app.listen(1245, () => {
  console.log('');
});

module.exports = app;
