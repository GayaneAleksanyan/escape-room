from functools import lru_cache
from collections import OrderedDict
from typing import Optional
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

if __name__ == "__main__":
    cache = LRUCache(2)
    print(cache.cache)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.cache)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.cache)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.cache)