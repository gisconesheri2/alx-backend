#!/usr/bin/env python3
"""
caching system with LFU system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ a dict based cache system without
    a limit of 4 items with a LFU mechanism
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
                # update use for the key
                val = self.use_order.get(key) + 1
                # move key to the end of the use dict
                del self.use_order[key]
                self.use_order[key] = val
            else:
                # get the least frequently used item in an Ordered Dict
                # sort the dict by values and get the first tuple
                # print(self.use_order)
                least_use = sorted(list(self.use_order.items())[0:BaseCaching.MAX_ITEMS],
                                   key=lambda x: x[1])[0]
                del self.cache_data[least_use[0]]
                del self.use_order[least_use[0]]
                print("DISCARD: {}".format(least_use[0]))
                self.cache_data[key] = item

    def get(self, key):
        """Get the value associated from the key
        Return: value associated with key or None
        """
        if key is None:
            return None
        val = self.cache_data.get(key, None)
        if val is not None:
            # update frequency use
            use = self.use_order.get(key) + 1
            # move key to the end of the ordered dict
            del self.use_order[key]
            self.use_order[key] = use
        return val
