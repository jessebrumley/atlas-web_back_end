# Pagination

## Introduction
This project focuses on implementing pagination techniques in Python for handling large datasets efficiently. Pagination is crucial for improving user experience and optimizing data retrieval by breaking down data into manageable pages. You will explore various pagination methods, including simple pagination, hypermedia pagination, and deletion-resilient pagination.

### Learning Objectives
By the end of this project, you should be able to explain the following concepts:
- How to paginate a dataset using simple `page` and `page_size` parameters.
- How to implement hypermedia metadata in pagination.
- How to create a deletion-resilient pagination system to handle dataset changes gracefully.

### Requirements
- All your files must be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.9).
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code must conform to `pycodestyle` standards (version 2.5.*).
- Documentation is required for all modules and functions.
- All functions and coroutines must be type-annotated.

### Setup
- Use the provided dataset file `Popular_Baby_Names.csv` for implementing pagination functionalities.

### Practical Tasks

**Task 0:** Simple Helper Function  
Create a function named `index_range` that takes two integer arguments, `page` and `page_size`. It should return a tuple containing the start index and end index for pagination. Page numbers are 1-indexed.

**Task 1:** Simple Pagination  
Implement a `Server` class that paginates the dataset of popular baby names. The `get_page` method should validate input and return the correct page of data based on pagination parameters.

**Task 2:** Hypermedia Pagination  
Enhance the `Server` class with a `get_hyper` method that returns additional metadata alongside the paginated data, including next and previous page information.

**Task 3:** Deletion-Resilient Hypermedia Pagination  
Develop a `get_hyper_index` method that allows pagination while accounting for potential deletions in the dataset. The method should provide data without skipping items even when rows are removed.

### Author
[Jesse Brumley](https://github.com/jessebrumley)
