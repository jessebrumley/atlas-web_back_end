#!/usr/bin/env node

/**
 * countStudents - reads database synchronously and returns student count
 * @param {string} path - the path to the database.csv
 */
const fs = require('fs');

function countStudents(path) {
  try {
    // Check if the file exists
    if (!fs.existsSync(path)) {
      console.error('File does not exist');
      return;
    }

    // Read the file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Filter out empty lines
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Check if the file is empty or invalid
    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    // Get the headers and the data
    const headers = lines[0].split(',').map(header => header.trim());
    const students = lines.slice(1).map(line => {
      const fields = line.split(',').map(field => field.trim());
      const student = {};
      headers.forEach((header, index) => {
        student[header] = fields[index];
      });
      return student;
    });

    // Calculate the total number of students
    const numberOfStudents = students.length;
    console.log(`Number of students: ${numberOfStudents}`);

    // Count the number of students in each field
    const fieldCount = {};
    students.forEach((student) => {
      const { field } = student;
      if (!fieldCount[field]) {
        fieldCount[field] = { count: 0, names: [] };
      }
      fieldCount[field].count += 1;
      fieldCount[field].names.push(student.firstname);
    });

    // Log the number of students in each field and their names
    Object.keys(fieldCount).forEach((field) => {
      const { count, names } = fieldCount[field];
      console.log(`Number of students in ${field}: ${count}. List: ${names.join(', ')}`);
    });
  } catch (error) {
    console.error('Cannot load the database');
  }
}

// If the script is called from the command line, we get the file path from arguments
if (require.main === module) {
  const path = process.argv[2];
  if (!path) {
    console.log('Usage: node 2-read_file.js <path_to_csv>');
    process.exit(1);
  }
  countStudents(path);
}

module.exports = countStudents;
