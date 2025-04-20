#!/usr/bin/env node

const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 3000;

const rawData = fs.readFileSync('data.json');
const data = JSON.parse(rawData);

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Welcome to the Music API');
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
