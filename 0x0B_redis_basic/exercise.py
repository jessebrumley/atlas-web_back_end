#!/usr/bin/env python3
import redis
import uuid
from typing import Callable, Optional, Union
import functools


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.

    Args:
        method: The function to be decorated.

    Returns:
        A wrapper function that logs inputs and outputs.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Create keys for input and output history
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Normalize args to string and store in Redis
        self._redis.rpush(input_key, str(args))

        # Call the original method
        output = method(self, *args, **kwargs)

        # Store the output in Redis
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


class Cache:
    def __init__(self) -> None:
        """Initialize the Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history  # Decorate the store method with call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a random key.

        Args:
            data: the data to be stored.

        Returns:
            the generated key as a string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Optional[Union[str, int, bytes]]:
        """
        Retrieve value from Redis and optionally convert to
        integer or string format.

        Args:
            key: the key to retrieve data for.
            fn: optional conversion function.

        Returns:
            the retrieved value or None if not found.
        """
        # retrieve value from Redis
        value = self._redis.get(key)

        # If no key, return None
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
