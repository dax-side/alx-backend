#!/usr/bin/env python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Least Recently Used Caching system"""
    def __init__(self):
        """" constructor"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """assign to the dictionary the item value for key key """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            discard = self.stack.pop(0)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        if key not in self.stack:
            self.stack.append(key)
        else:
            self.add_as_last_in(key=key)

    def get(self, key):
        """ return value from self.cache_data linked to key"""
        value = self.cache_data.get(key, None)
        if value is not None:
            self.add_as_last_in(key=key)
        return value

    def add_as_last_in(self, key):
        """Move an element to the end of the list"""
        if self.stack[-1] != key:
            self.stack.remove(key)
            self.stack.append(key)
