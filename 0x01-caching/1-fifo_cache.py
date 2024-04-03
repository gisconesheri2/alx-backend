#!/usr/bin/env python3
"""
caching system with FIFO system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ a dict based cache system without
    a limit of 4 items with a FIFO mechanism
    """

    def __init__(self):
        """Initialise the super class"""
        super().__init__()
        self.input_order = OrderedDict()

    def put(self, key, item):
        """Place a key in the dict"""
        if key is not None and item is not None:

            # update the input order dict
            if len(self.input_order) == 0:
                self.input_order[key] = 1
            else:
                val = sorted(self.input_order.values())[-1]
                self.input_order[key] = val + 1

            # check if length of cache exceeds set lenth
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            elif key in self.cache_data:
                self.cache_data[key] = item
            else:
                # get the first item in the Ordered Dict input order
                first_in = list(self.input_order.items())[0]
                del self.cache_data[first_in[0]]
                del self.input_order[first_in[0]]
                print("DISCARD: {}".format(first_in[0]))
                self.cache_data[key] = item

    def get(self, key):
        """Get the value associated from the key
        Return: value associated with key or None
        """
        if key is None:
            return None
        val = self.cache_data.get(key, None)
        return val
