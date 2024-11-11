class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.key_queue = []
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        # print(self.cache)
        if self.cache.get(key, -1) != -1:
            self.key_queue.remove(key)
            self.key_queue.append(key)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        # print(self.cache)
        if key in self.cache.keys():
            self.key_queue.remove(key)
        else:
            self.cache[key] = value 
            if len(self.cache) > self.capacity:
                del self.cache[self.key_queue[0]]
                self.key_queue = self.key_queue[1:]
        self.key_queue.append(key)
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)