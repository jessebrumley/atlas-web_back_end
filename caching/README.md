# Python - Caching Algorithms

## Introduction
This project focuses on implementing different caching algorithms in Python. Caching systems help optimize data retrieval by storing frequently accessed information in memory. You will explore various cache replacement policies, including FIFO, LIFO, LRU, MRU, and LFU. By the end, you should be able to understand the purpose of a caching system, its limitations, and how to implement key caching strategies.

### Learning Objectives
- Understand what a caching system is
- Learn about different cache replacement policies:
  - FIFO (First In, First Out)
  - LIFO (Last In, First Out)
  - LRU (Least Recently Used)
  - MRU (Most Recently Used)
  - LFU (Least Frequently Used)
- Know the purpose and limitations of a caching system

### Practical Tasks

**Task 0:** Basic Dictionary Cache  
You will create a `BasicCache` class that inherits from `BaseCaching`. This cache has no size limit.  
- `put(self, key, item)`: Assigns the value `item` to the `key` in the cache dictionary.
- `get(self, key)`: Returns the value associated with `key`, or `None` if the `key` is invalid.

**Task 1:** FIFO Caching  
You will create a `FIFOCache` class that inherits from `BaseCaching`. This cache follows the FIFO replacement policy.
- If the cache exceeds its size limit (`MAX_ITEMS`), the first added item is discarded.
- Print `DISCARD: <key>` when an item is removed.

**Task 2:** LIFO Caching  
You will create a `LIFOCache` class that inherits from `BaseCaching`. This cache follows the LIFO replacement policy.
- If the cache exceeds `MAX_ITEMS`, the last added item is discarded.
- Print `DISCARD: <key>` when an item is removed.

**Task 3:** LRU Caching  
You will create a `LRUCache` class that inherits from `BaseCaching`. This cache follows the LRU replacement policy.
- If the cache exceeds `MAX_ITEMS`, the least recently used item is discarded.
- Print `DISCARD: <key>` when an item is removed.

**Task 4:** MRU Caching  
You will create a `MRUCache` class that inherits from `BaseCaching`. This cache follows the MRU replacement policy.
- If the cache exceeds `MAX_ITEMS`, the most recently used item is discarded.
- Print `DISCARD: <key>` when an item is removed.

### Author
[Jesse Brumley](https://github.com/jessebrumley)
