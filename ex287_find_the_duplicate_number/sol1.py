from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]] # jump two steps

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow



    def findDuplicate_1(self, nums: List[int]) -> int:
        nums.sort()

        for i, x in enumerate(nums):
            if i == x:
                return i
        
        return 0



    def findDuplicate_bruteforce(self, nums: List[int]) -> int:

        if not nums:
            return 0

        for i, x in enumerate(nums):
            for y in nums[i+1:]:
                if x == y:
                    return x

        return 0

if __name__ == '__main__':
    sol = Solution()

    input_list = [
        [1, 3, 4, 2, 2],
        [3,1,3,4,2],
        [2,5,9,6,9,3,8,9,7,1]
    ]

    for inp in input_list:
        print("----")
        result_0 = sol.findDuplicate_bruteforce(inp)
        result = sol.findDuplicate(inp)
        print("solutions:")
        print(result, result_0)