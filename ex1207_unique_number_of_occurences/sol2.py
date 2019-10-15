from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return all(x==1 for x in Counter(Counter(arr).values()).values())


if __name__ == '__main__':

    arrs = [[1,2,2,1,1,3],
            [1,2],
            [-3,0,1,-3,1,1,1,-3,10,0]
            ]
    sol = Solution()

    for i, arr in enumerate(arrs):
        result = sol.uniqueOccurrences(arr)
        print(i, result)
