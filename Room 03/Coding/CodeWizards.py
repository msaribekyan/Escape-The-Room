# Create a Simple LRU (Least Recently Used) Cache. Build a class called LRUCache that simulates a basic "Least Recently Used" caching system. The cache has a fixed maximum size. When the cache is full and a new item is added, the least recently used item should be removed. Implement get(key) and put(key, value) methods.

# Note: You can use OrderedDict or manage a custom doubly-linked list.
from collections import OrderedDict
class LRUCache:
    def __init__(self,length):
        if length<=0 or not isinstance(length,int):
            raise ValueError("for length needs positive integer")
        self.length=length
        self.cache=OrderedDict()
    def put(self,key1,value1):
        if key1 is None or value1 is None:
            raise TypeError("Both key and value must be provided")
        if key1 in self.cache:
            self.cache.move_to_end(key1)
        elif len(self.cache)>=self.length:
            self.cache.popitem(last=False)
        self.cache[key1]=value1
    def get(self,key1):
        if key1 in self.cache:
            self.cache.move_to_end(key1)
            return self.cache[key1]
        else:
            return -1
try:
    cache=LRUCache(2)
    cache.put(1,1)# now OrderedDict([(1, 1)])
    cache.put(2,2)# now OrderedDict([(1, 1), (2, 2)])
    print(cache.get(1))#output is 1
    cache.put(3,3)#removes key  2 now OrderedDict([(1, 1), (3,3)])
    print(cache.get(2))# output -1 (not found)
except (ValueError,TypeError) as e:
    print(f"Invalid input:{e}")
