from sol2 import Solution

def test_1():
    sol = Solution()
    assert sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

def test_2():
    sol = Solution()
    assert sol.trap([2, 0, 2]) == 2

def test_3():
    sol = Solution()
    assert sol.trap([4,2,3]) == 1

def test_4():
    sol = Solution()
    assert sol.trap([2,1,0,2]) == 3

def test_5():
    sol = Solution()
    assert sol.trap([4,2,0,3,2,5]) == 9
    