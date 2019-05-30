from LRUCache2 import LRUCache

if __name__=='__main__':

    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.printQueue()

    #cache.get(3)
    cache.Q.remove(3)
    cache.printQueue()

