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

app.get('/genres', (req, res) => {
    const genres = data.genres.map(({ id, name }) => ({ id, name }));
    res.json(genres);
  });
  
  app.get('/genres/:id', (req, res) => {
    const genre = data.genres.find(g => g.id == req.params.id);
    if (!genre) return res.status(404).json({ error: 'Genre not found' });
    res.json(genre);
  });
  