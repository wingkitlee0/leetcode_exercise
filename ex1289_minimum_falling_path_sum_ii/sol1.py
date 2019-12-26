from typing import List

"""
Runtime: 860 ms, faster than 13.33% of Python3 online submissions for Minimum Falling Path Sum II.
Memory Usage: 15.7 MB, less than 100.00% of Python3 online submissions for Minimum Falling Path Sum II.

Note:
should optimize the finding of min for each j on the same row.

"""

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:

        nrow, ncol = len(A), len(A[0])

        if nrow == 1:
            return min(A[0])

        dp = [[float('inf')] * ncol for _ in range(nrow)]

        dp[-1][:] = A[-1] 

        for i in range(nrow-2, -1, -1):
            lst = dp[i+1]
            for j in range(ncol):
                lst = dp[i+1].copy()
                lst.pop(j)
                
                dp[i][j] = A[i][j] + min(lst)
                
        return min(dp[0])

def main():
    input_list = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ]

    sol = Solution()
    for inp in input_list:
        result = sol.minFallingPathSum(inp)
        print(result)


if __name__ == "__main__":
    main()
    
