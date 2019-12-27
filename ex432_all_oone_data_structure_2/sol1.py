from collections import defaultdict, deque
import heapq

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = defaultdict(int) # {key: count}
        self.ranks = defaultdict(set) # {count: keys}
        self.minKey = None
        self._lastmin = None
        self.maxKey = None
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """

        count = self.counter[key]
        self.counter[key] += 1

        self.ranks[count+1].add(key)
        if count > 0:
            self.ranks[count].remove(key)
            if len(self.ranks[count]) == 0:
                self.ranks.pop(count)

        if count == 0:
            self.minKey = key
        else:
            if self.minKey == key:
                if count in self.ranks and len(self.ranks[count]) > 0:
                    self.minKey = self.ranks[count].pop()
                    self.ranks[count].add(self.minKey)

        if self.maxKey is None:
            self.maxKey = key
        else:
            maxcount = self.counter[self.maxKey]
            if maxcount < count+1:
                self.maxKey = key

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.counter:
            return

        count = self.counter[key]
        maxcount = self.counter[self.maxKey]
        
        if count == 1:
            self.counter.pop(key)
        else:
            self.counter[key] -= 1

        self.ranks[count].remove(key)

        if count > 1:
            self.ranks[count-1].add(key)    
        # cleanup ranks if key-count is zero
        if len(self.ranks[count]) == 0:
            self.ranks.pop(count)

        if self.minKey not in self.counter:
            self.minKey = self._lastmin.pop()
            self._lastmin.add(self.minKey)

        # assign _lastmin if minKey has the same count with other key
        mincount = self.counter[self.minKey] # updated counter with updated minKey
        if mincount == count:
            self._lastmin = self.ranks[count]
            self.minKey = key
            print("_lastmin: ", self._lastmin)

        
        print("here", self.maxKey, maxcount, key, count)
        if maxcount == count:
            if count in self.ranks and len(self.ranks[count]) > 0:
                self.maxKey = self.ranks[count].pop()
                self.ranks[count].add(self.maxKey)        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return self.maxKey

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return self.minKey
        
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
        ('+', 'a'),
        ('+', 'b'),
        ('+', 'b'),
        ('+', 'c'),
        ('+', 'c'),
        ('+', 'c'),
        ('-', 'b'),
        ('-', 'b'),
        ('-', 'a'),
    ]

    obj = AllOne()

    for cmd in cmd_seq:
        if cmd[0] == '+':
            obj.inc(cmd[1])
            print("{}: {}; min = {}, max = {}".format(cmd, dict(obj.ranks), obj.getMinKey(), obj.getMaxKey()))
        if cmd[0] == '-':
            obj.dec(cmd[1])
            print("{}: {}; min = {}, max = {}".format(cmd, dict(obj.ranks), obj.getMinKey(), obj.getMaxKey()))

if __name__ == "__main__":
    main()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()