class Node:
    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None

class Queue3:
    """
    doubly-linked list implementation with:
    - O(1) node removal
    - capacity
    
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.head = None
        self.last = None
        self.dict = {}

    def printQueue(self):
        r = self.head
        while r is not None:
            print(r.x)
            r = r.next

    def push(self, x):
        newnode = Node(x)

        if self.length == self.capacity:
            self.pop()

        if self.head is None:
            self.head = newnode
            self.last = self.head
        else:
            r = self.last
            r.next = newnode
            newnode.prev = r
            self.last = newnode

        self.dict[x[0]] = newnode
        self.length += 1

    def pop(self):
        """
        remove node closest to head
        """
        if self.head is not None:
            r = self.head
            x = r.x

            if self.last == self.head:
                self.head = None
                self.last = None
            else:
                self.head = r.next
                self.head.prev = None
        
            self.dict.pop(x[0]) # remove key from dictionary
            self.length -= 1
            return x

    def remove(self, key):
        print("calling remove")
        if self.head is not None:
            if key in self.dict:
                node = self.dict[key]
                
                if self.length == 1:
                    print("len = 1")
                    self.head = None
                    self.last = None
                else:
                    if node == self.head:
                        self.head = node.next
                        self.head.prev = None
                        #if node == self.last:
                        #    print("--remove-- head=last=node!", self.length, len(self.dict) )
                        #    self.head = None
                        #    self.last = None
                        #else:
                        #    self.head = node.next
                        #    self.head.prev = None
                    elif node == self.last:
                        node.prev.next = None
                        self.last = node.prev
                        self.last.next = None
                    else:
                        next = node.next
                        prev = node.prev
                        prev.next = next
                        next.prev = prev
                print("here2")
                self.dict.pop(key)
                self.length -= 1

if __name__ == '__main__':
    Q = Queue3(4)
    for i in [1,2,3,4,5]:
        Q.push([i])

    Q.pop()
    Q.printQueue()
    print("---")
    Q.remove(3)
    Q.printQueue()
    print("---")
    Q.push([8])
    while Q.head is not None:
        print(Q.pop(), Q.length)

            