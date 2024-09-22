# Personal Data Management

## Introduction
This project involves implementing methods for securely managing personal data and handling sensitive information. The focus is on identifying Personally Identifiable Information (PII), logging data safely by obfuscating PII, encrypting passwords, and securely connecting to a database. These techniques ensure that sensitive information is handled properly while logging and authenticating, thereby adhering to best practices for data security.

### Learning Objectives
By the end of this project, you should be able to:
- Identify examples of Personally Identifiable Information (PII)
- Implement a log filter that obfuscates PII fields in log records
- Encrypt a password and check the validity of an input password
- Authenticate to a database using environment variables

### Requirements
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.9).
- Files must end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should conform to `pycodestyle` standards (version 2.5.*).
- All modules, classes, and functions must include documentation.
- Functions should be type-annotated.

### Practical Tasks

**Task 0:** Regex-ing  
Create a function `filter_datum` that uses regex to obfuscate specified fields in a log message. It should replace occurrences of PII fields with a redacted string.

**Task 1:** Log Formatter  
Create a `RedactingFormatter` class that formats log records, using the `filter_datum` function to filter PII from log messages.

**Task 2:** Create Logger  
Implement a `get_logger` function that returns a logger object configured to log up to `INFO` level and use the `RedactingFormatter` to filter sensitive fields from logs.

**Task 3:** Connect to Secure Database  
Write a `get_db` function to securely connect to a database using credentials stored in environment variables.

**Task 4:** Read and Filter Data  
Implement a main function that retrieves data from the `users` table in the database and logs the results while filtering sensitive fields.

**Task 5:** Encrypt Passwords  
Write a `hash_password` function to securely hash passwords using the `bcrypt` library.

**Task 6:** Check Valid Password  
Create an `is_valid` function to check if an input password matches a previously hashed password using `bcrypt`.

### Author
[Jesse Brumley](https://github.com/jessebrumley)
```