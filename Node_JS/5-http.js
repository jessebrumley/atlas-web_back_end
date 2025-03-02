#!/usr/bin/env node

// Project notes: the project asks us to use the countStudents function within
// the server but does not explain what to do when importing the database.
// So instead of hardcoding it to use the one, I made it so that the database is
// loaded directly from the url. Also errors and console logs are shown client side

const http = require('http');
const countStudents = require('./3-read_file_async');

// Create an HTTP server
const app = http.createServer(async (req, res) => {
  const url = req.url;

  // Store original console functions
  const originalLog = console.log;
  const originalError = console.error;

  // Buffer to capture the logs and errors
  let logBuffer = '';

  // Override console.log to capture logs and write to both client and server
  console.log = (message) => {
    logBuffer += message + '\n';
    process.stdout.write(message + '\n');
  };

  // Override console.error to capture errors and write to both client and server
  console.error = (message) => {
    logBuffer += message + '\n';
    process.stderr.write(message + '\n');
  };

  if (url === '/') {
    // Route for / (root)
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!\n');
  } else if (url === '/students') {
    // Route for /students (no database)
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Please enter a student database. Example: /students/database.csv\n');
  } else if (url.startsWith('/students/')) {
    // Route that imports database from the URL
    const dbPath = url.split('/')[2];

    try {
      // Await the result from countStudents
      const result = await countStudents(dbPath);

      // Ensure result is returned as a string, if not already
      const resultText = result ? result.toString() : '';

      // Send the captured logs and the result to the client
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/plain');
      res.end(logBuffer + resultText); // Append the logBuffer to the result

    } catch (error) {
      // Handle any errors that countStudents throws (such as file not found)
      console.error(`Error: ${error.message}`);
      res.statusCode = 500;
      res.end(`Error: ${error.message}\n`);
    }
  } else {
    // For any other path, respond with "Not Found"
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not Found\n');
  }

  // Restore original console functions
  console.log = originalLog;
  console.error = originalError;
});

// The server listens on port 1245
app.listen(1245, () => {
  console.log('Server is running on http://localhost:1245');
});

// Server is assigned and exported to the variable app
module.exports = app;
