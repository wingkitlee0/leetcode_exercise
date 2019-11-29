from sol1 import Solution

def test_LIS_1():
    assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4

def test_LIS_2():
    assert Solution().lengthOfLIS([10,9,2,5,3,4]) == 3

def test_LIS_3():
    assert Solution().lengthOfLIS([2,2]) == 1

def test_LIS_4():
    assert Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]) == 6