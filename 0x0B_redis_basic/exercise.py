#!/usr/bin/env python3
import redis
import uuid
from typing import Callable, Optional, Union

class Cache:
    def __init__(self) -> None:
        """Initialize the Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a random key

        Args:
            data: the data to be stored
        Returns:
            the generated key as a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, int, bytes]]:
        """
        Retrieve value from Redis and optionally converts to
        integer or string format

        Args:
            data: the data to be stored
        Returns:
            the generated key as a string
        """
        # retrieve value from Redis
        value = self._redis.get(key)
        
        # If no key, return none
        if value is None:
            return None
        
        # apply convert functionn
        if fn is not None:
            return fn(value)
        
        # return as is
        return value

    def get_str(self, key: str) -> Optional[str]:
        # call get method and convert to string
        return self.get(key, lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)

    def get_int(self, key: str) -> Optional[int]:
        # Call get method and convert to integer
        return self.get(key, lambda x: int(x))