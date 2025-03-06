#!/usr/bin/env node

const express = require('express');
const app = express();

app.use(express.json());

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

app.get('/available_payments', (req, res) => {
    res.json({
      payment_methods: {
        credit_cards: true,
        paypal: false,
      },
    });
  });

  app.post('/login', (req, res) => {
    const { userName } = req.body;
    res.status(200).send(`Welcome ${userName}`);
  });

module.exports = app;
