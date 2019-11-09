from typing import List
from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        result = [[]]
        for i, c in counts.items():
            result = [ r + [i]*j for r in result for j in range(0, c+1)]
        return result

if __name__ == '__main__':
    sol = Solution()

    input_list = [
        [1, 2, 2]
    ]

    for inp in input_list:
        result = sol.subsetsWithDup(inp)
        print(result)