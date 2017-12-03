"""Inverted index implementation
to store entities collected from the documents"""

from collections import defaultdict

class InvertedIndex(object):
    """Inverted index for entities"""
    def __init__(self):
        self.idx = defaultdict(lambda: [])

    def add(self, key, elem):
        """Adds a element to the index at the given key"""
        self.idx[key].append(elem)

    def count(self, key):
        """Gives count of particular key"""
        return len(self.idx[key])
