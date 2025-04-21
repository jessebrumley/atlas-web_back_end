#!/usr/bin/env node

const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 3000;

// data
const rawData = fs.readFileSync('data.json');
const data = JSON.parse(rawData);

app.use(express.json());

// routes
app.get('/', (req, res) => {
  res.send('Welcome to the Music API');
});

// List all genres
app.get('/genres', (req, res) => {
  const genres = data.genres.map(({ id, name }) => ({ id, name }));
  res.json(genres);
});

// Get genre by ID or name
app.get('/genres/:identifier', (req, res) => {
  const { identifier } = req.params;
  let genre;

  if (/^\d+$/.test(identifier)) {
    // checks if identifier is a number using Regex
    genre = data.genres.find(g => g.id == parseInt(identifier));
  } else {
    // Otherwise assumes a string as a name
    genre = data.genres.find(g => g.name.toLowerCase() === identifier.toLowerCase());
  }

  if (!genre) {
    return res.status(404).json({ error: 'Genre not found' });
  }

  res.json(genre);
});

// server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
