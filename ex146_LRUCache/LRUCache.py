"""
Implement a LRUCache

- using a Queue, which is implemented using a doubly-linked list.
"""

class Node:
    def __init__(self, key, value):
        self.x = {key: value}
        self.next = None
        self.prev = None
        self.age = 0

class Queue:
    def __init__(self):
        #self.capacity = capacity
        self.head = None
        self.last = None
        self.dict = {}

    def pop(self):
        """
        pop item in the queue (far from the head)
        """
        if self.last is None:
            return None
        else:
            k, v = self.last.x.popitem()

            # fix DLL
            if self.head == self.last:
                self.head = None
            else:
                self.last, self.last.next = self.last.prev, None
                if self.last == self.head:
                    self.last.prev = None
                
            # fix dict
            self.dict.pop(k, None)
            return v
    
    def push(self, key, value, age):
        """
        push item
        """
        newnode = Node(key, value)
        newnode.age = age
        
        if self.head is None:
            self.head = newnode
            self.last = newnode
        else:
            newnode.next = self.head
            self.head = newnode
            newnode.next.prev = newnode
            
        self.dict[key] = newnode

    def remove(self,key):
        """
        remove a specific item with key
        """
        #print("remove {}".format(key))
        if key in self.dict:
            node = self.dict[key]

            if node == self.last:
                self.pop()
            else:
                if self.head == node:
                    self.head = node.next
                else:
                    node.prev.next = node.next
           
            # fix dict
            self.dict.pop(key, None)
            
    @property
    def length(self):
        return len(self.dict)

    def printQueue(self):
        r = self.head
        while r is not None:
            print(r.x)
            r = r.next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.age = 0
        self.Q = Queue()
        

    def get(self, key: int) -> int:
        if key in self.Q.dict:
            node = self.Q.dict[key]
            value = node.x[key]
            self.age += 1
            self.Q.remove(key)
            #self.Q.printQueue()
            self.Q.push(key, value, self.age) # refresh
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Q.dict:
            self.Q.remove(key)

        if self.Q.length >= self.capacity:
            print("the queue is full. popping one ")
            r = self.Q.pop() # remove the oldest
            self.Q.printQueue()
            print(r)
        
        self.Q.push(key, value, self.age)
        self.age += 1

    def printQueue(self):
        print("Q: ")
        node = self.Q.head
        while node is not None:
            print(node.x, node.age)
            node = node.next
        print("---")




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    queue = Queue()
    queue.push(1,1,0)
    print(queue.dict.keys())
    r = queue.pop()
    print(r)
    print(queue.dict)
    queue.push(1,1,0)
    queue.push(2,1,0)
    queue.push(3,1,0)
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
    print('C', cache.Q.dict['C'].age)