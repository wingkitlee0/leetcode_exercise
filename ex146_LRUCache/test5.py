from LRUCache2 import LRUCache

if __name__=='__main__':

    cache = LRUCache(2)
    cache.put(2, 1)
    cache.get(2)
    cache.printQueue()

    #cache.get(3)
#    cache.Q.remove(3)
#    cache.printQueue()

