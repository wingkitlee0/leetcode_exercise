from typing import List

"""
longest increasing subsequence

- non-contiguous elements
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        returns the length of longest increasing subsequence

        Note:
            - O(n^2) algorithm
        """

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [None] * n
        dp[0] = 1

        for i in range(1, n):
            dp_ = [(nums[j], dp[j]) for j in range(i) if nums[j] < nums[i]]
            #print(dp_)
            if dp_ == []:
                dp[i] = 1
            else:
                dp[i] = 1 + max([k for _, k in dp_])

            print("{}: {}".format(nums[i], dp))
        return max(dp)
        

        
        
        
if __name__ == '__main__':
    input_list = [
        [10,9,2,5,3,7,101,18], # 4
        [10,9,2,5,3,4],
        [2,2], # 1
        [1,3,6,7,9,4,10,5,6], # 6
    ]

    sol = Solution()
    for inp in input_list:
        result = sol.lengthOfLIS(inp)
        print(result)