#!/usr/bin/python3
"""
BasicCache module implements a basic caching system with no size limit.
This class inherits from BaseCaching and uses a
dictionary to store key-value pairs.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class provides a caching system without size constraints.
    It inherits from BaseCaching, which provides a cache_data dictionary.
    """
    def put(self, key: str, item: str) -> None:
        """
        Store the item in the cache_data dictionary.
        If key or item is None, this method does nothing.

        Args:
            key (str): The key for the cache.
            item (str): The item to cache.
        """
        # Adds item to cached data
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: str) -> str | None:
        """
        Retrieve the item associated with the given key from
        the cache_data dictionary.
        If the key is None or not found, return None.

        Args:
            key (str): The key to look up in the cache.

        Returns:
            str | None: The value associated with the key,
            or None if the key is not found.
        """
        # fetches item held in cached_data
        return self.cache_data.get(key) if key in self.cache_data else None
