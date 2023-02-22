#!/usr/bin/env python3
""" caching sytem module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching implements a caching system
        implements the put and get method defined in the Base class
    """
    def put(self, key, item):
        """ assigns value for the key to a dictionary self.cache_data"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
