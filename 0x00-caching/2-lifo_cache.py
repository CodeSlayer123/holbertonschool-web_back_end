#!/usr/bin/env python3
"""task 2 task 2 task 2 task 2 task 2 task 2"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """task 2 task 2 task 2 task 2 task 2 task 2"""
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.latest = ""

    def put(self, key, item):
        """sets an item"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD:", self.latest)
                del self.cache_data[self.latest]
            self.latest = key

    def get(self, key):
        """gets an item"""

        if key is None:
            return None
        try:
            return self.cache_data[key]
        except:
            return None
