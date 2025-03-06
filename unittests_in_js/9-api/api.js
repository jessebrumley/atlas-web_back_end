#!/usr/bin/env node

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (req, res) => {
  const { id } = req.params;
  res.send(`Payment methods for cart ${id}`);
});

app.use('/cart/:id', (req, res) => {
  res.status(404).send();
});

app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
