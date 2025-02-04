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

    def get(
        self,
        ey: str,
        fn: Optional[Callable] = None
    ) -> Optional[Union[str, int, bytes]]:
# Retrieve the value from Redis
        value = self._redis.get(key)
        
        # If the key does not exist, return None
        if value is None:
            return None
        
        # If a callable function is provided, apply it to the value
        if fn is not None:
            return fn(value)
        
        # Otherwise, return the value as it is (byte string)
        return value

    def get_str(self, key: str) -> Optional[str]:
        # Use the get method with a conversion to string (UTF-8)
        return self.get(key, lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)

    def get_int(self, key: str) -> Optional[int]:
        # Use the get method with a conversion to integer
        return self.get(key, lambda x: int(x))

# Example Usage
if __name__ == "__main__":
    cache = Cache()

    # Assume a key-value pair is stored in Redis like so:
    # cache._redis.set('my_str_key', 'hello world')
    # cache._redis.set('my_int_key', 123)

    # Testing get_str and get_int
    print(cache.get_str('my_str_key'))
    print(cache.get_int('my_int_key'))