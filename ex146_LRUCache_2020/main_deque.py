from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque() # keep track of the order
        self.cache = dict() # key: index
        
    def get(self, key: int) -> int:
        if len(self.cache) == 0:
            return -1
        
        if key in self.cache:
            result = self.cache[key]
            # move key to the front
            self.queue.remove(key)
            self.queue.appendleft(key)
            return result
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            # move key to the front
            self.queue.remove(key)
            self.queue.appendleft(key)
        else:
            if len(self.cache) >= self.capacity:
                lru_key = self.queue.pop()
                self.cache.pop(lru_key)

            self.cache[key] = value
            self.queue.appendleft(key)

    def summarize(self):
        print("cache: ", self.cache)
        print("queue: ", self.queue)

def main():  
    lru_cache = LRUCache(capacity=2)
    lru_cache.put(1, 1)
    lru_cache.summarize()
    lru_cache.put(2, 2)
    lru_cache.summarize()
    r = lru_cache.get(1)
    print(r)
    lru_cache.summarize()
    lru_cache.put(3, 3)
    lru_cache.summarize()
    r = lru_cache.get(2)
    print(r)
    lru_cache.put(4, 4)
    lru_cache.summarize()
    r = lru_cache.get(1)
    print(r)
    r = lru_cache.get(3)
    print(r)
    r = lru_cache.get(4)
    print(r)


if __name__ == "__main__":
    main()