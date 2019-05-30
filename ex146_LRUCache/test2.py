from LRUCache import LRUCache

#["LRUCache","get","put","get","put","put","get","get"]
#[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

if __name__ == '__main__':

    l1 = ["LRUCache","get","put","get","put","put","get","get"]
    l2 = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

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