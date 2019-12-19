from collections import defaultdict
from math import sqrt, ceil

class Solution:
    def minSteps(self, n: int) -> int:

        if n == 0:
            return -1
        if n == 1:
            return 0
        if n == 2:
            return 2
        
        _dict = defaultdict(int)
        while n % 2 == 0:
            _dict[2] += 1
            n = n // 2

        # prime factor > 2
        n_ = n
        for i in range(3, n // 2, 2):
            while n % i == 0:
                _dict[i] += 1
                n = n // i

        if n_ == n and n > 2:
            _dict[n] += 1 # if n is a prime

        result = sum([k*v for k, v in _dict.items()])

        if result == 0:
            return n
        else:
            return result 


if __name__ == '__main__':

    sol = Solution()
    for i in range(1, 35):
        result = sol.minSteps(i)
        print("{}: {}".format(i, result))