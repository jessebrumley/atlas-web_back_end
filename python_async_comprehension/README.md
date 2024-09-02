# Python - Async Comprehension

## Introduction
This project focuses on mastering Python's asynchronous programming capabilities through practical tasks. You will implement and refine asynchronous generators and comprehensions, culminating in measuring the runtime for parallel executions. By the end, you should be able to create asynchronous generators, utilize async comprehensions effectively, and understand their performance implications.

### Learning Objectives
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

### Practical Tasks
**Task 0:** Async Generator - A coroutine called async_generator that takes no arguments.The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10.

**Task 1:** Async Comprehensions -  A coroutine called async_comprehension that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

**Task 2:** Run time for four parallel comprehensions - A measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather. measure_runtime should measure the total runtime and return it.

**Task 3:** Tasks - Write a function task_wait_random that takes an integer max_delay and returns a asyncio.Task.

### Author
[Jesse Brumley](https://github.com/jessebrumley)
