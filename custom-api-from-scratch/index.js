#!/usr/bin/env node

const express = require('express');
const fs = require('fs');
const winston = require('winston');
const swaggerJSDoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');
const swaggerFile = require('./swagger-output.json');

const app = express();
const PORT = 3000;

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerFile));

// Swagger definition
const swaggerDefinition = {
  openapi: '3.0.0',
  info: {
    title: 'My API',
    version: '1.0.0',
    description: 'API documentation for my project'
  },
  servers: [
    {
      url: 'http://localhost:3000',
    },
  ],
};

// Options for the swagger-jsdoc
const options = {
  swaggerDefinition,
  apis: ['./index.js'], // Path to the API docs (could be other JS files if needed)
};

// Initialize swagger-jsdoc
const swaggerSpec = swaggerJSDoc(options);

// Use swagger-ui-express to serve the API docs
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));

// winston logger
const logger = winston.createLogger({
  level: 'info',
  transports: [
    new winston.transports.Console({ format: winston.format.simple() })
  ],
});

logger.info('Logger is set up!');

// data
const rawData = fs.readFileSync('data.json');
const data = JSON.parse(rawData);

app.use(express.json());

/**
 * @swagger
 * /:
 *   get:
 *     description: Welcome message
 *     responses:
 *       200:
 *         description: Welcome to the Music API
 */
app.get('/', (req, res) => { // routes
  logger.info('Home accessed');
  res.send('Welcome to the Music API');
});

/**
 * @swagger
 * /genres:
 *   get:
 *     description: List all genres
 *     responses:
 *       200:
 *         description: A list of all genres
 */
app.get('/genres', (req, res) => { // List all genres
  const genres = data.genres.map(({ id, name }) => ({ id, name }));
  logger.info('Genres accessed');
  res.json(genres);
});

/**
 * @swagger
 * /genres/{identifier}:
 *   get:
 *     description: Get genre by ID or name
 *     parameters:
 *       - name: identifier
 *         in: path
 *         required: true
 *         description: The genre ID or name
 *         schema:
 *           type: string
 *       - name: includeAlbums
 *         in: query
 *         description: Include album details
 *         schema:
 *           type: string
 *       - name: includeSongs
 *         in: query
 *         description: Include song details
 *         schema:
 *           type: string
 *       - name: includeAll
 *         in: query
 *         description: Include both albums and songs
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: Genre details
 *       404:
 *         description: Genre not found
 */
app.get('/genres/:identifier', (req, res) => { // Get genre by ID or name
  const { identifier } = req.params;
  const { includeAlbums, includeSongs, includeAll } = req.query;
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

  const genreCopy = { ...genre };

  genreCopy.artists = (genre.artists || []).map(artist => {
    let artistBase = { id: artist.id, name: artist.name };
  
    // Add albums if requested
    if (includeAll === 'true' || includeAlbums === 'true' || includeSongs === 'true') {
      artistBase.albums = (artist.albums || []).map(album => {
        const albumBase = {
          id: album.id,
          title: album.title,
          release_year: album.release_year
        };
  
        if (includeAll === 'true') {
          albumBase.songs = (album.songs || []).map(song => ({
            id: song.id,
            title: song.title,
            duration: song.duration,
            preview: song.preview
          }));
        } else if (includeSongs === 'true') {
          albumBase.songs = (album.songs || []).map(song => song.title);
        }
  
        return albumBase;
      });
    }
  
    return artistBase;
  });
  
  logger.info('Genres/ accessed');
  res.json(genreCopy);
  
});

/**
 * @swagger
 * /artists:
 *   get:
 *     description: List all artists
 *     responses:
 *       200:
 *         description: A list of all artists
 */
app.get('/artists', (req, res) => { // List all artists
  const artists = data.genres.flatMap(genre =>
    (genre.artists || []).map(({ id, name }) => ({ id, name }))
  );
  logger.info('Artists accessed');
  res.json(artists);
});

/**
 * @swagger
 * /artists/{identifier}:
 *   get:
 *     description: Get artist by ID or name, with optional albums and songs
 *     parameters:
 *       - name: identifier
 *         in: path
 *         required: true
 *         description: The artist ID or name
 *         schema:
 *           type: string
 *       - name: includeAlbums
 *         in: query
 *         description: Include album details
 *         schema:
 *           type: string
 *       - name: includeSongs
 *         in: query
 *         description: Include song details
 *         schema:
 *           type: string
 *       - name: includeAll
 *         in: query
 *         description: Include both albums and songs
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: Artist details
 *       404:
 *         description: Artist not found
 */
app.get('/artists/:identifier', (req, res) => { // Get artist by ID or name
  const { identifier } = req.params;
  const { includeAlbums, includeSongs, includeAll } = req.query;
  let artist;

  for (const genre of data.genres) {
    const found = (genre.artists || []).find(a =>
      /^\d+$/.test(identifier)
        ? a.id == parseInt(identifier)
        : a.name.toLowerCase() === identifier.toLowerCase()
    );
    if (found) {
      artist = found;
      break;
    }
  }

  if (!artist) {
    return res.status(404).json({ error: 'Artist not found' });
  }

  const artistCopy = { ...artist };

  if (includeAlbums === 'true' || includeSongs === 'true' || includeAll === 'true') {
    artistCopy.albums = (artist.albums || []).map(album => {
      const base = {
        id: album.id,
        title: album.title,
        year: album.year
      };

      if (includeAll === 'true') {
        return {
          ...base,
          songs: (album.songs || []).map(song => ({
            id: song.id,
            title: song.title,
            duration: song.duration,
            preview: song.preview
          }))
        };
      }

      if (includeSongs === 'true') {
        return {
          ...base,
          songs: (album.songs || []).map(song => song.title)
        };
      }

      return base;
    });
  } else {
    delete artistCopy.albums;
  }

  logger.info('Artists accessed');
  res.json(artistCopy);
});

/**
 * @swagger
 * /artists/{identifier}/albums:
 *   get:
 *     description: Get albums by artist's ID or name
 *     parameters:
 *       - name: identifier
 *         in: path
 *         required: true
 *         description: The ID or name of the artist
 *         schema:
 *           type: string
 *       - name: includeSongs
 *         in: query
 *         description: Include song titles in album response
 *         schema:
 *           type: string
 *           enum: [true, false]
 *       - name: includeAll
 *         in: query
 *         description: Include full album details (songs and more)
 *         schema:
 *           type: string
 *           enum: [true, false]
 *     responses:
 *       200:
 *         description: A list of albums for the artist
 *       404:
 *         description: Artist not found
 */
app.get('/artists/:identifier/albums', (req, res) => { // Get albums by artist's ID or name
  const { identifier } = req.params;
  const { includeSongs, includeAll } = req.query;
  let artist;

  for (const genre of data.genres) {
    artist = genre.artists.find(a =>
      /^\d+$/.test(identifier)
        ? a.id == parseInt(identifier)
        : a.name.toLowerCase() === identifier.toLowerCase()
    );
    if (artist) break;
  }

  if (!artist) {
    return res.status(404).json({ error: 'Artist not found' });
  }

  let albums = artist.albums || [];

  if (includeAll === 'true') {
    albums = albums.map(album => ({
      id: album.id,
      title: album.title,
      year: album.year,
      songs: (album.songs || []).map(song => ({
        id: song.id,
        title: song.title,
        duration: song.duration,
        preview: song.preview
      }))
    }));
  } else {
    if (includeSongs === 'true') {
      albums = albums.map(album => ({
        id: album.id,
        title: album.title,
        year: album.year,
        songs: (album.songs || []).map(song => song.title)
      }));
    } else {
      albums = albums.map(({ id, title, year }) => ({ id, title, year }));
    }
  }
  logger.info('Albums accessed');
  res.json(albums);
});


/**
 * @swagger
 * /albums/{identifier}:
 *   get:
 *     description: Get album by ID or title
 *     parameters:
 *       - name: identifier
 *         in: path
 *         required: true
 *         description: The ID or title of the album
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: Album details
 *       404:
 *         description: Album not found
 */
/**
 * @swagger
 * /albums/{identifier}/songs:
 *   get:
 *     description: Get songs for a specific album by album ID or title
 *     parameters:
 *       - name: identifier
 *         in: path
 *         required: true
 *         description: The ID or title of the album
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: A list of songs in the album
 *       404:
 *         description: Album not found
 */
app.get(['/albums/:identifier', '/albums/:identifier/songs'], (req, res) => {
  const { identifier } = req.params; // Get all songs for a specific album
  let album;

  for (const genre of data.genres) {
    for (const artist of genre.artists) {
      album = artist.albums.find(a =>
        /^\d+$/.test(identifier)
          ? a.id === parseInt(identifier)
          : a.title.toLowerCase() === identifier.toLowerCase()
      );
      if (album) break;
    }
    if (album) break;
  }

  if (!album) {
    return res.status(404).json({ error: 'Album not found' });
  }
  logger.info('Albums and songs accessed');
  res.json(album.songs || []);
});

/**
 * @swagger
 * /artists/{artistIdentifier}/albums/{albumIdentifier}:
 *   get:
 *     description: Get album by ID or title for a specific artist
 *     parameters:
 *       - name: artistIdentifier
 *         in: path
 *         required: true
 *         description: The ID or name of the artist
 *         schema:
 *           type: string
 *       - name: albumIdentifier
 *         in: path
 *         required: true
 *         description: The ID or title of the album
 *         schema:
 *           type: string
 *       - name: includeAll
 *         in: query
 *         description: Include full album details (songs and more)
 *         schema:
 *           type: string
 *           enum: [true, false]
 *     responses:
 *       200:
 *         description: Album details including songs
 *       404:
 *         description: Artist or album not found
 */
/**
 * @swagger
 * /artists/{artistIdentifier}/albums/{albumIdentifier}/songs:
 *   get:
 *     description: Get songs for a specific album by ID or title for a specific artist
 *     parameters:
 *       - name: artistIdentifier
 *         in: path
 *         required: true
 *         description: The ID or name of the artist
 *         schema:
 *           type: string
 *       - name: albumIdentifier
 *         in: path
 *         required: true
 *         description: The ID or title of the album
 *         schema:
 *           type: string
 *       - name: includeAll
 *         in: query
 *         description: Include full album details (songs and more)
 *         schema:
 *           type: string
 *           enum: [true, false]
 *     responses:
 *       200:
 *         description: List of song titles in the album
 *       404:
 *         description: Artist or album not found
 */
app.get( 
  [ // Find the artist by ID or name
    '/artists/:artistIdentifier/albums/:albumIdentifier',
    '/artists/:artistIdentifier/albums/:albumIdentifier/songs'
  ],
  (req, res) => {
    const { artistIdentifier, albumIdentifier } = req.params;
    const { includeAll } = req.query;
    let artist;

    for (const genre of data.genres) {
      artist = genre.artists.find(a =>
        /^\d+$/.test(artistIdentifier)
          ? a.id == parseInt(artistIdentifier)
          : a.name.toLowerCase() === artistIdentifier.toLowerCase()
      );
      if (artist) break;
    }

    if (!artist) {
      return res.status(404).json({ error: 'Artist not found' });
    }

    const album = (artist.albums || []).find(alb =>
      /^\d+$/.test(albumIdentifier)
        ? alb.id == parseInt(albumIdentifier)
        : alb.title.toLowerCase() === albumIdentifier.toLowerCase()
    );

    if (!album) {
      return res.status(404).json({ error: 'Album not found for the specified artist' });
    }

    if (includeAll === 'true') {
      return res.json({
        artist: {
          id: artist.id,
          name: artist.name,
        },
        album: {
          id: album.id,
          title: album.title,
          year: album.year,
          songs: album.songs || [],
        }
      });
    }

    const songTitles = (album.songs || []).map(song => song.title);
    res.json(songTitles);
  }
);

/**
 * @swagger
 * /songs/{identifier}:
 *   get:
 *     description: Get song by ID or title
 *     parameters:
 *       - name: identifier
 *         in: path
 *         required: true
 *         description: The ID or title of the song
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: Song details
 *       404:
 *         description: Song not found
 */
app.get('/songs/:identifier', (req, res) => { // Get song(s) by ID or title
  const { identifier } = req.params;
  let song;

  for (const genre of data.genres) {
    for (const artist of genre.artists) {
      for (const album of artist.albums) {
        song = album.songs.find(s =>
          /^\d+$/.test(identifier)
            ? s.id === parseInt(identifier)
            : s.title.toLowerCase() === identifier.toLowerCase()
        );
        if (song) break;
      }
      if (song) break;
    }
    if (song) break;
  }

  if (!song) {
    return res.status(404).json({ error: 'Song not found' });
  }

  logger.info('Songs accessed');
  res.json({
    id: song.id,
    title: song.title,
    duration: song.duration,
    preview: song.preview
  });
});

// testing
module.exports = app;

// server
app.listen(PORT, () => {
  logger.info(`Server is running on http://localhost:${PORT}`);
});
