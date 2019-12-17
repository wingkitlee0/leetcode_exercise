from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = defaultdict(int, [])
        n = len(nums)
        
        while nums:
            x = nums.pop()
            if counter[x] >= n/2:
                return x
            else:
                counter[x] += 1

        for k, v in counter.items():
            if v >= n/2:
                return k

def test_1():
    sol = Solution()
    assert sol.majorityElement([1,2,2]) == 2