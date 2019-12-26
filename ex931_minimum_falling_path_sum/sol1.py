from typing import List

"""
Runtime: 124 ms, faster than 76.92% of Python3 online submissions for Minimum Falling Path Sum.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Minimum Falling Path Sum.
"""

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:

        nrow, ncol = len(A), len(A[0])

        if nrow == 1:
            return min(A[0])

        dp = [[float('inf')] * ncol for _ in range(nrow)]

        dp[-1][:] = A[-1] 

        for i in range(nrow-2, -1, -1):
            for j in range(ncol):
                lst = [dp[i+1][j] ]
                if j > 0:
                    lst.append( dp[i+1][j-1] )
                if j < ncol-1:
                    lst.append( dp[i+1][j+1] )

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
    
