# Redis Basics Project
This repository contains exercises that demonstrate how to use Redis for basic operations and caching in Python. Below are the details for each task.

---

## 1. Basic Authentication API

### Introduction
The Redis Basics project is designed to help you learn and practice Redis commands, Python integration with Redis, and use cases like caching and data storage. This project provides hands-on tasks that focus on writing to Redis, reading data, and managing lists with Redis.

### Learning Objectives
By the end of this project, you should be able to:
- Use Redis for basic operations.
- Use Redis as a simple cache.
- Write and retrieve data in Redis using Python.
- Store lists and manage data histories.

### Practical Tasks

**Task 0:** Writing strings to Redis
* Create a Cache class that stores data in Redis.
* Implement a store method to generate a random key, store the data, and return the key.

**Task 1:** Reading from Redis and recovering original type
* Implement a get method with an optional callable to convert data back to its original format.
* Add methods get_str and get_int for automatic type conversion.

**Task 2:** Incrementing values
* Implement a count_calls decorator to track how many times a method is called.

**Task 3:** Storing lists
* Implement a call_history decorator to store input and output lists for functions.

**Task 4:** Retrieving lists
* Create a replay function to display the history of calls to a particular function.

### Author
[Jesse Brumley](https://github.com/jessebrumley)
