#!/usr/bin/env python3
"""exercise file that contains Cache class"""
import redis
import uuid
from typing import Callable
import functools

def count_calls(method:Callable ) -> Callable:
    """the count calls function"""
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper

def call_history(method:Callable) -> Callable:
    """the call history function"""

    @functools.wraps(method)
    def wrapper(self, *args):
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args)
        self._redis.rpush(f"{key}:outputs", output)
        return output
    return wrapper

def replay(method: Callable):
    """replays inputs and outputs"""

    _redis = redis.Redis()
    key = method.__qualname__
    inputs = _redis.lrange(f"{key}:inputs", 0, -1)
    outputs = _redis.lrange(f"{key}:outputs", 0, -1)
    count = len(inputs)
    print(f"{key} was called {count} times:")
    for i, j in zip(inputs, outputs):
        print(f"{key}(*{i.decode('utf-8')}) -> {(j).decode('utf-8')}")

class Cache():
    """Cache class inside exercise file"""

    def __init__(self):
        """the init class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: str or bytes or int or float) -> str:
        """generates random key and stores in Reids"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """redis get function"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key):
        """converts redis response to str"""
        Cache.get(key, str)

    def get_int(self, key):
        """converts redis response to int"""

        Cache.get(key, int)
