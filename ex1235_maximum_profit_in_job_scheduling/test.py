class Memo:
    """
    this is a dictionary that keeps tracks of the min and max
    the setter should only set a key that is smaller than current keys    
    """
    _first = True
    def __init__(self):
        self._dp = dict()
        self.key_max = float('inf')
        self.key_min = float('-inf')

    def __getitem__(self, key):
        if key > self.key_max:
            return self._dp[self.key_max]
        else:
            if key < self.key_min:
                return self._dp[self.key_min]
            else:
                return self._dp[key] # let it raise error if key is not there

    def __setitem__(self, key, value):
        if self._first:
            self.key_max = key
            self.key_min = key
            self._dp[key] = value
            self._first = False
        else:
            if key >= self.key_max:
                raise KeyError("New key must be smaller than the first key.")
            else:
                if key >= self.key_min:
                    raise KeyError("New key must be smaller than the min key")
                else:
                    self.key_min = key
                    self._dp[key] = value

if __name__ == '__main__':
    memo = Memo()
    memo[2] = 2
    memo[1] = 1
    for i in range(4):
        print("{}: {}".format(i, memo[i]))