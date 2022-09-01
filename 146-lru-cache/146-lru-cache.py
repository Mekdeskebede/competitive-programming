class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = OrderedDict()
        
    def get(self, key: int) -> int:
        
        
        if key in self.lru:
            value = self.lru.pop(key)
            self.lru[key] = value
            return self.lru[key]
        else:
            return -1   

    def put(self, key: int, value: int) -> None:
        
        if key in self.lru:
            self.lru.pop(key)
            self.lru[key] = value
            return
        if len(self.lru) == self.capacity:
            self.lru.popitem(last = False)
            self.lru[key] = value
        else:
            self.lru[key] = value
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
