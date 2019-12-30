from typing import List
from collections import defaultdict

"""
Runtime: 1640 ms, faster than 5.07% of Python3 online submissions for Maximum Profit in Job Scheduling.
Memory Usage: 62.9 MB, less than 100.00% of Python3 online submissions for Maximum Profit in Job Scheduling.
"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        st_d = defaultdict(list)
        for i, x in enumerate(startTime):
            st_d[x].append(i)
        
        print(st_d)

        ndp = max(endTime) # length of dp array

        dp = [0] * (ndp+1) # initialize a zero dp array

        currmax = 0
        for i in range(ndp-1, -1, -1): # backward
            if i not in st_d:
                dp[i] = dp[i+1]
            else:
                max_ = max([profit[j] + dp[endTime[j]] for j in st_d[i]])
                currmax = max(max_, currmax)
                dp[i] = currmax

            print(i, dp[i])


        return dp[0]

def main():
    input_list = [
        [[1,2,3,3], [3,4,5,6], [50,10,40,70]], # 120
        [[1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]], # 150
        [[1,1,1], [2,3,4], [5,6,4]], # 6
    ]

    sol = Solution()
    for inp in input_list:
        result = sol.jobScheduling(*inp)
        print(inp, result)


if __name__ == "__main__":
    main()
