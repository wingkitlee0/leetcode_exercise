from LRUCache2 import LRUCache

if __name__ == '__main__':

    l1 = ["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
    l2 = [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]

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