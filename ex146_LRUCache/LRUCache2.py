"""
Implement a LRUCache

- using a Queue, which is implemented using a doubly-linked list.
"""

from queue3 import Queue3 as Queue

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.age = 0
        self.Q = Queue(capacity)
        
    def get(self, key: int) -> int:
        if key in self.Q.dict:
            node = self.Q.dict[key]
            value = node.x[1]
            self.age += 1
            self.Q.remove(key)
            self.Q.push([key, value, self.age]) # refresh
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Q.dict:
            self.Q.remove(key)
            
        if self.Q.length >= self.capacity:
            self.Q.pop()
        
        self.Q.push([key, value, self.age])
        self.age += 1

    def printQueue(self):
        print("Q: ")
        node = self.Q.head
        while node is not None:
            print(node.x)
            node = node.next
        print("---")




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    queue = Queue(10)
    queue.push([1,1,0])
    print(queue.dict.keys())
    r = queue.pop()
    print(r)
    print(queue.dict)
    queue.push([1,1,0])
    queue.push([2,1,0])
    queue.push([3,1,0])
    print(queue.dict.keys())
    queue.remove(2)
    print(queue.dict.keys())
    print(queue.length)

    cache = LRUCache(4)

    for s in 'ABCDEDF':
        cache.put(s,s)
    
    cache.printQueue()
    
    print( cache.Q.length)
    print('A', cache.get('A'))
    cache.printQueue()
    print('B', cache.get('B'))
    print('C', cache.get('C'))
    print('C', cache.Q.dict['C'].x[2])