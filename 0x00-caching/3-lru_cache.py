#!/usr/bin/env python3
"""task 3 task 3 task 3 task 3 task 3"""
from base_caching import BaseCaching
import collections


class LRUCache(BaseCaching):
    """task 3 task 3 task 3 task 3 task 3 task 3"""
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = collections.OrderedDict(self.cache_data)

    def put(self, key, item):
        """sets an item"""
        self.get(key)

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            deleted = self.cache_data.popitem(last=False)
            print("DISCARD", deleted[0])

    def get(self, key):
        """gets an item"""

        if key is None:
            return None
        try:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        except:
            return None
