"""
Implement a LRUCache

- using a Queue, which is implemented using a doubly-linked list.
"""

from queue3 import Queue3 as Queue

class LRUCache:
    """
    Version 3 of LRU Cache
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.age = 0
        self.queue = Queue(capacity)

    def get(self, key: int) -> int:
        """
        Args:
            key: int
        Return: int
        """
        if key in self.queue.dict:
            node = self.queue.dict[key]
            value = node.x[1]
            self.age += 1
            self.queue.remove(key)
            self.queue.push([key, value, self.age]) # refresh
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Args:
            key, value: int
        Return: None
        """
        if key in self.queue.dict:
            self.queue.remove(key)

        if self.queue.length >= self.capacity:
            self.queue.pop()

        self.queue.push([key, value, self.age])
        self.age += 1

    def print_queue(self):
        """
        print out the current queue
        Args: None
        """
        print("Q: ")
        node = self.queue.head
        while node is not None:
            print(node.x)
            node = node.next
        print("---")




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    """
    main function for example usage
    """
    queue = Queue(10)
    queue.push([1, 1, 0])
    print(queue.dict.keys())
    _r = queue.pop()
    print(_r)
    print(queue.dict)
    queue.push([1, 1, 0])
    queue.push([2, 1, 0])
    queue.push([3, 1, 0])
    print(queue.dict.keys())
    queue.remove(2)
    print(queue.dict.keys())
    print(queue.length)

    cache = LRUCache(4)

    for _c in 'ABCDEDF':
        cache.put(_c, _c)

    cache.print_queue()
    print(cache.queue.length)
    print('A', cache.get('A'))
    cache.print_queue()
    print('B', cache.get('B'))
    print('C', cache.get('C'))
    print('C', cache.queue.dict['C'].x[2])

if __name__ == '__main__':
    main()
