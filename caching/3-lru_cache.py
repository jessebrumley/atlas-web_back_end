#!/usr/bin/python3
""" LRUCache Implementation without move_to_end
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Implements an LRU Cache:
        - Adds items to cache_data using the LRU strategy
        - Retrieves items from cache_data
    """

    def __init__(self):
        """ Initializes the LRUCache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Inserts an item into cache_data

            Args:
            - self: Instance of the class
            - key: Key for the item
            - item: Item to be inserted into cache_data

            Return:
            - None
        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            # If key already exists, remove it first
            del self.cache_data[key]
        
        # Add the item to the end of the cache_data
        self.cache_data[key] = item

        # If the cache exceeds the maximum allowed items, remove the oldest item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))
            self.cache_data.pop(oldest_key)
            print(f'DISCARD: {oldest_key}')

    def get(self, key):
        """ Retrieves an item from cache_data

            Args:
            - self: Instance of the class
            - key: Key for the item

            Return:
            - Item from cache_data associated with the key
            - None if the key is not found or is None
        """

        if key is None:
            return None

        if key in self.cache_data:
            # Move this item to the end to mark it as recently used
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
        return None
