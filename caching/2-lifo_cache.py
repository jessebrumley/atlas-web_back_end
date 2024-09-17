#!/usr/bin/python3
""" A Last In, First Out (LIFO) caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ LIFOCache class implements a Last In, First Out (LIFO) caching system
    """

    def __init__(self):
        """ Initialize the LIFOCache class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache

        Args:
            key: The item key
            item: The item to be added

        Return:
            None
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.cache_data.popitem(last=True)
            print(f"DISCARD: {next(reversed(self.cache_data))}")

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache.

        Args:
            key: The key for the item.

        Return:
            The item if found, otherwise None.
        """
        if key is None:
            return None

        return self.cache_data.get(key)
