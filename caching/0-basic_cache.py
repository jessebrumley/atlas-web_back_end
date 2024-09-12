#!/usr/bin/env python3
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

    def __init__(self) -> None:
        """Initialize the BasicCache instance by calling
        the parent class constructor."""
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """
        Store the item in the cache_data dictionary.
        If key or item is None, this method does nothing.

        Args:
            key (str): The key for the cache.
            item (str): The item to cache.
        """
        # Prevents null/empty values
        if key is None or item is None:
            return
        # Adds item to cached data
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
