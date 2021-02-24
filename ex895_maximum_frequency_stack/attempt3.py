from collections import deque, defaultdict

class FreqStack:
    def __init__(self):
        self.counter = {} # key: count
        self.data = defaultdict(deque) # (key, value) = (count, stack)
        
    def push(self, x: int) -> None:

        if x in self.counter:
            new_count = self.counter[x] + 1
            self.counter[x] = new_count
            self.data[new_count].append(x)

        else:
            self.counter[x] = 1
            self.data[1].append(x)

    def pop(self) -> int:
        if len(self.counter) == 0:
            return None

        max_count = len(self.data) # the bucket is continuous
        x = self.data[max_count].pop()
        self.counter[x] -= 1
        
        # clean up the empty stack at old max_count
        if len(self.data[max_count]) == 0:
            del self.data[max_count]
        
        return x


            

        
        