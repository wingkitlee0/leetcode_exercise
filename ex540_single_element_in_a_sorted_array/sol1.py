"""
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once. Find this single element that appears only once.

Note:  Your solution should run in O(log n) time and O(1) space.
"""
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        print(nums)
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return nums[0]
        if n % 2 == 0:
            return None
        
        # n must be odd
        mid = (n-1) // 2 # index of the middle element

        if (mid+1) % 2 == 0: 
            # length of nums[:mid+1] is even
            if nums[mid-1] == nums[mid]: 
                # unique num in second half
                return self.singleNonDuplicate(nums[mid+1:])
            else:
                # unique num in first half
                return self.singleNonDuplicate(nums[:mid])
        else:
            # length of nums[:mid+1] is odd
            if nums[mid-1] == nums[mid]: 
                return self.singleNonDuplicate(nums[:mid-1])
            else:
                return self.singleNonDuplicate(nums[mid:])
        


        #return None

if __name__ == '__main__':
    
    input_list = [
        [1,1,2,3,3,4,4,8,8], # 2
        [3,3,7,7,10,11,11], # 10
        [1,1,2,3,3,4,4], # 2
    ]

    sol = Solution()
    for inp in input_list:
        result = sol.singleNonDuplicate(inp)
        print(result)