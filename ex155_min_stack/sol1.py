class MinStack:
    def __init__(self):
        """
        init your data structure here
        """
        self.stack = []

    def push(self, x):
        """
        """
        if self.stack == []:
            self.stack = [(x, x)]
        else:
            curr_val, curr_min = self.stack[-1]
            if x < curr_min:
                self.stack.append( (x, x))
            else:
                self.stack.append( (x, curr_min))

    def pop(self):
        curr_val, _ = self.stack.pop()
        return curr_val

    def top(self):
        top_val, _ = self.stack[0]
        return top_val

    def getMin(self):
        _, curr_min = self.stack[-1]
        return curr_min



