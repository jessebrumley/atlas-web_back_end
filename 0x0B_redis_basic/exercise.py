#!/usr/bin/env python3
import redis
import uuid
from typing import Union

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
