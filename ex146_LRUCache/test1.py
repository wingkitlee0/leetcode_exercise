from LRUCache import LRUCache

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1);
    cache.printQueue()
    cache.put(2, 2);
    cache.printQueue()
    print(cache.get(1)) # 1
    cache.printQueue()
    cache.put(3, 3)
    cache.printQueue()
    print(cache.get(2))
    print(cache.Q.dict)