#!/usr/bin/env python3
"""task 1 task 1 task 1 task 1 task 1"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """task 1 task 1 task 1 task 1 task 1 task 1"""
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """sets an item"""
        keys = list(self.cache_data)
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD:", keys[0])
                del self.cache_data[keys[0]]


    def get(self, key):
        """gets an item"""

        if key is None:
            return None
        try:
            return self.cache_data[key]
        except:
            return None
