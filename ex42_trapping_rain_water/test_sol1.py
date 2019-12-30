from sol1 import Solution

def test_1():
    sol = Solution()
    assert sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

def test_2():
    sol = Solution()
    assert sol.trap([2, 0, 2]) == 2
    