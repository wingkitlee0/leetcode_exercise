from collections import defaultdict, deque


class Node:
    """
    A single node of a doubly-linked list
    """
    def __init__(self, count, first_key):
        self.count = count
        self.keys = set([first_key])
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = {} # {key: Node}
        self.head = None # min
        self.last = None # max
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        
        if len(self.counter) > 0:
            assert self.head is not None and self.last is not None

        if key not in self.counter: # new key
            if len(self.counter) == 0: # new data structure
                self.counter[key] = Node(count=1, first_key=key)
                self.head = self.counter[key]
                self.last = self.counter[key]
            else:
                if self.head.count == 1:
                    assert len(self.head.keys) >= 1
                    self.head.keys.add(key)
                else:
                    assert self.head.count > 1
                    new_head = Node(count=1, first_key=key)
                    self.head.prev = new_head
                    new_head.next = self.head
                    self.head = new_head
                self.counter[key] = self.head
        else:
            curr = self.counter[key]
            count = curr.count

            #print(f"inc({key})! ", curr.count, curr.keys)
            if len(curr.keys) == 1:
                if curr.next is None:
                    # if current node has only one key, increase the count by 1
                    assert self.last == curr
                    curr.count += 1
                else:
                    curr.keys.remove(key)
                    if curr.next.count == curr.count+1:
                        curr.next.keys.add(key) 
                        self.counter[key] = curr.next
                        if self.head == curr:
                            self.head = self.counter[key]
                    else:
                        new_node = Node(count+1, key)
                        new_node.next = curr.next
                        new_node.prev = curr
                        curr.prev.next = new_node
                        curr.next.prev = new_node
                        self.counter[key] = new_node


            elif len(curr.keys) > 1:
                curr.keys.remove(key) # remove key from current node
                #print(f"curr.keys after removing {key}: {curr.keys}")
                if curr.next is None:
                    assert self.last == curr # only the last node does not have self.next
                    #print(f"inc({key})!! ", curr.count)
                    new_node = Node(count=count+1, first_key=key)
                    curr.next = new_node; new_node.prev = curr
                    self.last = new_node
                    self.counter[key] = new_node
                else:
                    # curr.next is not None
                    if curr.next.count == count+1:
                        curr.next.keys.add(key) 
                        self.counter[key] = curr.next
                    else:
                        assert curr.next.count > count+1 # next.count should be greater than count+1
                        new_node = Node(count=count+1, first_key=key)
                        far_node = curr.next
                        new_node.prev = curr; new_node.next = far_node 
                        curr.next = new_node; far_node.prev = new_node
                        self.counter[key] = new_node
                        
            else:
                raise AttributeError(f"curr.keys should not be empty (key={key})")

#        print("head = ", self.head.count, self.head.keys)
#        print("last = ", self.last.count, self.last.keys)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """

        if key not in self.counter:
            return # do nothing if key does not exist

        curr = self.counter[key]
        assert len(curr.keys) >= 1 and curr.count >= 1

        if curr == self.head:
            if len(curr.keys) == 1:
                if curr.count == 1:
                    # shift head if possible, otherwise cleanup
                    self.counter.pop(key)

                    if curr.next is None:
                        # clean up
                        self.head = None
                        self.last = None
                        assert len(self.counter) == 0
                    else:
                        # shift head
                        self.head = curr.next
                        self.head.prev = None
                else:
                    # curr.count > 1, keep the node
                    curr.count -= 1 # decrease curr.count by 1
            else:
                # len(curr.keys) > 1
                curr.keys.remove(key) # remove key
                
                if curr.count == 1:
                    self.counter.pop(key) # remove key from counter
                else:
                    new_node = Node(curr.count-1, key)
                    new_node.next = curr
                    curr.prev = new_node
                    self.head = new_node
        else:
            assert curr.count > 1 # if count == 1, it should be head as well..
            if len(curr.keys) == 1:
                if curr.prev.count == curr.count-1:
                    curr.prev.keys.add(key) # add key to prev when the count is right
                    if curr == self.last:
                        # update last node
                        curr.prev.next = None 
                        self.last = curr.prev
                    else:
                        # skip the current node with the to-be-removed key
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                    self.counter[key] = curr.prev
                    curr = None
                else:
                    assert curr.prev.count < curr.count-1
                    # only single key, keep the node and decreate the count
                    curr.count -= 1
            else:
                assert len(curr.keys) > 1
                curr.keys.remove(key)
                if curr.prev.count == curr.count-1:
                    curr.prev.keys.add(key) # add key to prev when the count is right
                    # no need to update last node as there are other keys
                    self.counter[key] = curr.prev
                else:
                    assert curr.prev.count < curr.count-1
                    # insert a new node
                    new_node = Node(curr.count-1, key)
                    new_node.next = curr; new_node.prev = curr.prev
                    curr.prev.next = new_node; curr.prev = new_node
                    self.counter[key] = new_node

#        print("head = ", self.head.count, self.head.keys)
#        print("last = ", self.last.count, self.last.keys)
        
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.last is not None:
            maxKey = self.last.keys.pop()
            self.last.keys.add(maxKey)
            return maxKey
        else:
            return ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.head is not None:
            minKey = self.head.keys.pop()
            self.head.keys.add(minKey)
            return minKey
        else:
            return ""

    def __str__(self):
        #return " ".join([f"({k},{v.count})" for k, v in self.counter.items()])
        lst = []
        node = self.head
        while node:
            lst.append(f"{node.count}:{node.keys}")
            node = node.next
        return " ".join(lst)
        
def main():
    cmd_seq = [
        # ('+', 'a'),
        # ('+', 'c'),
        # ('+', 'a'),
        # ('+', 'a'),
        # ('+', 'b'),
        # ('+', 'b'),
        # ('-', 'a'),
        # ('-', 'a'),
        # ('+', 'c'),
        # ('+', 'a'),
        # ('+', 'b'),
        # ('+', 'c'),
        # ('+', 'd'),
        # ('+', 'a'),
        # ('+', 'b'),
        # ('+', 'c'),
        # ('+', 'd'),
        # ('+', 'c'),
        # ('+', 'd'),
        # ('+', 'd'),
        # ('+', 'a'),
        ('+', 'h'),
        ('+', 'w'),
        ('+', 'h'),
        ('-', 'w'),
        ('+', 'h'),
        ('+', 'l'),
        ('-', 'h'),
        ('-', 'h'),
        ('-', 'h'),
    ]

    obj = AllOne()

    for cmd in cmd_seq:
        if cmd[0] == '+':
            obj.inc(cmd[1])
            print("{}: {}; min = {}, max = {}".format(cmd, obj, obj.getMinKey(), obj.getMaxKey()))
            
        if cmd[0] == '-':
            obj.dec(cmd[1])
            print("{}: {}; min = {}, max = {}".format(cmd, obj, obj.getMinKey(), obj.getMaxKey()))
        print("----")

if __name__ == "__main__":
    main()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()