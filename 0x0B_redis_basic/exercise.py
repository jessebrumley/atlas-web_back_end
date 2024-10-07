#!/usr/bin/env python3
import redis
import uuid
from typing import Callable, Optional, Union
import functools


class Cache:
    def __init__(self) -> None:
        """Initialize the Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable) -> Callable:
        """
        Counts the number of times a method is called

        Args:
            method: The method to check

        Returns:
            The method that increments a call count in Redis.
        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            # Use the method's name to create a Redis key for counting
            key = method.__qualname__
            
            # Increment the count for this method in Redis
            self._redis.incr(key)
            
            # Call the original method and return its result
            return method(self, *args, **kwargs)
        
        return wrapper

    @count_calls  # Decorate the store method with count_calls
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

        # apply convert function
        if fn is not None:
            return fn(value)

        # return as is
        return value

    def get_str(self, key: str) -> Optional[str]:
        # call get method and convert to string
        return self.get(
            key,
            lambda x: (
                x.decode('utf-8') if isinstance(x, bytes) else x
            )
        )

    def get_int(self, key: str) -> Optional[int]:
        # Call get method and convert to integer
        return self.get(key, lambda x: int(x))
