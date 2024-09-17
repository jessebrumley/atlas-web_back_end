#!/usr/bin/python3
""" MRUCache implements a Most Recently Used (MRU) caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache implements a Most Recently Used (MRU) caching system
    """

    def __init__(self):
        """ Initializes the MRUCache instance
        """
        super().__init__()
        self.cache_data = {}

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

        # If the key already exists, update the item
        if key in self.cache_data:
            del self.cache_data[key]

        # If the cache is full, discard the most recently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the most recently used item
            most_recent_key = next(reversed(self.cache_data))
            self.cache_data.pop(most_recent_key)
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

        # Retrieve the item if it exists
        if key in self.cache_data:
            # Move accessed item to the end to mark it as most recently used
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item

        return None
