#!/usr/bin/python3
"""
Test
"""
import sys

try:
    LFUCache = __import__('100-lfu_cache').LFUCache
    from base_caching import BaseCaching

    BaseCaching.MAX_ITEMS = 1
    LFUCache.MAX_ITEMS = 1
    my_cache = LFUCache()
    my_cache.MAX_ITEMS = 1
    prev_key = None
    
    for i in range(5):
        key = "key-{}".format(i)
        value = "value-{}".format(i)
        my_cache.put(key, value)
        if prev_key is not None:
            my_cache.get(key)
        prev_key = key
        my_cache.print_cache()

except:
    print(sys.exc_info()[1])