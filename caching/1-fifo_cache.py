#!/usr/bin/python3
"""
FIFOCache module implements a FIFO caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    BasicCache class provides a caching system without size constraints.
    It inherits from BaseCaching, which provides a cache_data dictionary.
    """
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds item to the cache_data dictionary
        Removes oldest item is dict contains too many items
        """

        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {self.stack[0]}")
                del self.cache_data[self.order[0]]
                self.order.pop(0)
            self.cache_data.update({key: item})
            self.stack.append(key)

    def get(self, key):
        """
        Retrieve the item associated with the given key from
        the cache_data dictionary.
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
