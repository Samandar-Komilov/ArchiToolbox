"""
HASHTABLE IMPLEMENTATION
In this code, I'll try to implement a hashtable class, with collision handling techniques I know:
- Separate Chaining
- Linear Probing
- Quadratic Probing
- Double Hashing
"""

from typing import Hashable


class Hashtable:
    def __init__(self, size = 10):
        self.size = size
        self.map = [[] for _ in range(size)]
    
    def __hash(self, key):
        return hash(key)

    def print(self):
        for e in self.map:
            print(e)
    
    """Separate Chaining Method"""
    def put(self, key: Hashable, value: any):
        idx = self.__hash(key) % self.size
        # self.map[idx].append((key, value))
        for i, (k, v) in enumerate(self.map[idx]):
            if k == key:
                self.map[idx][i] = (key, value)
                return None
        self.map[idx].append((key, value))
    
    def get(self, key: Hashable):
        idx = self.__hash(key) % self.size
        for k, v in self.map[idx]:
            if k == key:
                return v
        return None
    
    def delete(self, key: Hashable):
        idx = self.__hash(key) % self.size
        for i, (k, v) in enumerate(self.map[idx]):
            if k == key:
                return self.map[idx].pop(i)[1]
        return None
    

ht = Hashtable()
ht.put("one", 1)
ht.put("one", 3)
ht.put("two", 2)
ht.put("three", 13)
ht.print()
print(ht.get("three"))
ht.delete("two")
ht.print()