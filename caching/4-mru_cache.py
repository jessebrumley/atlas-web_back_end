#!/usr/bin/python3
""" MRUCache implements a Most Recently Used (MRU) caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache implements a Most Recently Used (MRU) caching system
    """

    def __init__(self):
        """ Initializes the MRUCache instance
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Adds an item to the cache

            Args:
            - key: Key for the item
            - item: Item to be added to the cache

            Returns:
            - None
        """
        if key is None or item is None:
            return

        # Remove the most recently used item if the cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recent_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {most_recent_key}")

        # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache

            Args:
            - key: Key for the item

            Returns:
            - The item associated with the key, or None if key doesn't exist
        """
        if key is None:
            return None

        return self.cache_data.get(key)
