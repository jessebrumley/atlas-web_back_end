# Node Express

## Description  
This project is a simple Express server that handles student data from a CSV file. It provides API routes to retrieve student counts and lists based on their field of study.


## Resources
Read or watch:
- Node JS getting started
- Process API doc
- Child process
- Express getting started
- Mocha documentation
- Nodemon documentation

## Learning Objectives
By the end of this project, you should be able to:
- Run JavaScript using Node.js
- Use Node.js modules
- Read files with specific Node.js modules
- Access command-line arguments and the environment using `process`
- Create a small HTTP server with Node.js
- Develop advanced routes using Express.js
- Use ES6 features with Babel-node
- Utilize Nodemon for faster development

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`, Visual Studio Code
- Interpreted/compiled on Ubuntu 18.04 LTS using Node.js (version 12.x.x)
- All files should end with a new line
- A `README.md` file is mandatory at the root of the project folder
- JavaScript files must use the `.js` extension
- Code will be tested using Jest (`npm run test`)
- Code will be verified with ESLint
- Code must pass all tests and linting (`npm run full-test`)
- Functions/classes must be exported using `module.exports = myFunction;`

## Provided Files
- `database.csv` (Student data)
- `package.json`
- `babel.config.js`
- `.eslintrc.js`

**Don't forget to run `npm install` after cloning the repository!**

## Tasks

### 0. Executing Basic JavaScript with Node.js
- Create `0-console.js`.
- Implement `displayMessage` function that prints a string to STDOUT.

### 1. Using Process stdin
- Create `1-stdin.js`.
- Prompt the user with `Welcome to Holberton School, what is your name?`.
- Read input and display `Your name is: INPUT`.
- On exit, print `This important software is now closing`.

### 2. Reading a File Synchronously with Node.js
- Create `2-read_file.js`.
- Implement `countStudents` function to read `database.csv` synchronously.
- Log the total student count and distribution by field.
- Throw an error if the file cannot be read.

### 3. Reading a File Asynchronously with Node.js
- Create `3-read_file_async.js`.
- Implement `countStudents` function to read `database.csv` asynchronously.
- Return a Promise.
- Log student distribution or throw an error if the file cannot be read.

### 4. Create a Basic HTTP Server
- Create `4-http.js`.
- Use Node's `http` module to create a server.
- Listen on port `1245` and respond with `Hello Holberton School!`.

### 5. Create a More Complex HTTP Server
- Create `5-http.js`.
- Handle `/` route with `Hello Holberton School!`.
- Handle `/students` route by reading `database.csv` asynchronously and displaying student distribution.
- Listen on port `1245`.

### 6. Create a Basic HTTP Server with Express
- Install `express`.
- Create `6-http_express.js`.
- Implement an Express server listening on port `1245`.
- Serve `Hello Holberton School!` on the root route.

### 7. Create a More Complex HTTP Server with Express
- Create `7-http_express.js`.
- Implement Express routes:
  - `/`: Returns `Hello Holberton School!`
  - `/students`: Returns student distribution from `database.csv`.
- Listen on port `1245`.

### 8. Organize a Full Express Server
- Create `full_server/` directory.
- Implement:
  - `utils.js`: `readDatabase` function (async student file reading).
  - `controllers/AppController.js`: `getHomepage` method.
  - `controllers/StudentsController.js`: `getAllStudents` and `getAllStudentsByMajor`.
  - `routes/index.js`: Define `/`, `/students`, and `/students/:major`.
  - `server.js`: Initialize Express and use routes.
- Use `babel-node` for ES6 compatibility.
- Run with `nodemon --exec babel-node --presets babel-preset-env ./full_server/server.js ./database.csv`.


## Author
[Jesse Brumley](https://github.com/jessebrumley)
