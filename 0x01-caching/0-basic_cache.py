#!/usr/bin/env python3
"""
basic caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ a dict based cache system without
    a limit
    """

    def __init__(self):
        """Initialise the super class"""
        super().__init__()

    def put(self, key, item):
        """Place a key in the dict"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get the value associated from the key
        Return: value associated with key or None
        """
        if key is None:
            return None
        val = self.cache_data.get(key, None)
        return val
