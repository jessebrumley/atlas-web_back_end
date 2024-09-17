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
        self.usage_order = []

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

        # If key already exists, update the item and mark it as recently used
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_order.remove(key)
        else:
            # Remove the most recently used item if the cache is full
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_recent_key = self.usage_order.pop()
                self.cache_data.pop(most_recent_key)
                print(f"DISCARD: {most_recent_key}")

            # Add the new item to the cache
            self.cache_data[key] = item

        # Mark the key as most recently used
        self.usage_order.insert(0, key)

    def get(self, key):
        """ Retrieves an item from the cache

            Args:
            - key: Key for the item

            Returns:
            - The item associated with the key, or None if key doesn't exist
        """
        if key is None:
            return None

        # Retrieve the item if it exists and mark it as most recently used
        if key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.insert(0, key)
            return self.cache_data[key]

        return None
