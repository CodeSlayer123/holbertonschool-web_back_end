#!/usr/bin/env python3
"""task 0"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """task 0"""
    def __init__(self):
        """ Initiliaze
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """sets an item"""

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """gets an item"""

        if key is None:
            return None
        try:
            return self.cache_data[key]
        except:
            return None
