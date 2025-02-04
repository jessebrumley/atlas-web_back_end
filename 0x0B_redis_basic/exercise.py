#!/usr/bin/env python3
import redis
import uuid
from typing import Callable, Optional, Union
import functools


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""
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

    def count_calls(method: Callable) -> Callable:
        """Counts the number of times a method is called."""
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
    @call_history  # Also decorate with call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis with a random key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Optional[Union[str, int, bytes]]:
        """Retrieve value from Redis and optionally convert to int or str"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Call get method and convert to string."""
        return self.get(
            key,
            lambda x: x.decode('utf-8') if isinstance(x, bytes) else x
        )

    def get_int(self, key: str) -> Optional[int]:
        """Call get method and convert to integer."""
        return self.get(key, lambda x: int(x))


def replay(cache: Cache, method: Callable) -> None:
    """Display the history of calls for a particular method."""
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)

    call_count = len(inputs)
    print(f"{method.__qualname__} was called {call_count} times:")

    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{eval(inp)}) -> {out.decode('utf-8')}")
