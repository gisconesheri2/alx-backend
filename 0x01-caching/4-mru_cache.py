#!/usr/bin/env python3
"""
caching system with LIFO system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ a dict based cache system without
    a limit of 4 items with a LIFO mechanism
    """

    def __init__(self):
        """Initialise the super class"""
        super().__init__()
        self.use_order = OrderedDict()

    def put(self, key, item):
        """Place a key in the dict"""
        if key is not None and item is not None:
            if key not in self.use_order:
                self.use_order[key] = 0

            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            elif key in self.cache_data:
                self.cache_data[key] = item
                del self.use_order[key]
                self.use_order[key] = 0
            else:
                # get the last item in the Ordered Dict input order
                most_use = list(self.use_order.items())[-2]
                del self.cache_data[most_use[0]]
                del self.use_order[most_use[0]]
                print("DISCARD: {}".format(most_use[0]))
                self.cache_data[key] = item

    def get(self, key):
        """Get the value associated from the key
        Return: value associated with key or None
        """
        if key is None:
            return None
        val = self.cache_data.get(key, None)
        if val is not None:
            del self.use_order[key]
            self.use_order[key] = 0
        return val
