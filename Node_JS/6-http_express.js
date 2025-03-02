#!/usr/bin/env node

const express = require('express');
const app = express();

// Route for / (root)
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Listen on port 1245
app.listen(1245, () => {
  console.log('');
});

module.exports = app;
