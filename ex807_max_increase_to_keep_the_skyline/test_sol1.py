from sol1 import Solution

def test_example1():
    sol = Solution()
    assert sol.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]) == 35
