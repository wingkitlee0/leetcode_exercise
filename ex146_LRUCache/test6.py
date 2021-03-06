from LRUCache2 import LRUCache

if __name__ == '__main__':

    l1 = ["LRUCache","put","get","put","get","get"]
    l2 = [[1],[2,1],[2],[3,2],[2],[3]]
    
    for cmd, arg in zip(l1, l2):
        if cmd == "LRUCache":
            cache = LRUCache(arg[0])
        if cmd == "get":
            print("get", arg[0])
            r = cache.get(arg[0])
            print(r)
        if cmd == "put":
            print("put", arg)
            cache.put(arg[0], arg[1])
                
        cache.printQueue()