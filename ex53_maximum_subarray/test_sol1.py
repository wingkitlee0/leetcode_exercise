from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        sarr = [0] * len(nums)
        sarr[0] = nums[0]
        for i in range(1, n):
            sarr[i] = sarr[i-1] + nums[i]

        print("sarr = ", sarr)
        j_max = 0; _max = float('-inf')
        for i, x in enumerate(sarr):
            if x > _max:
                j_max = i
                _max = x

        i_min = 0; _min = float('inf')
        for i, x in enumerate(sarr):
            if x < _min:
                i_min = i
                _min = x

        print(_min, _max)
        #if _max < 0 and _min < 0:
        #    return _min - _max
        if i_min > j_max:
            return _min - _max
        return _max - _min




def test_1():
    sol = Solution()
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_2():
    sol = Solution()
    assert sol.maxSubArray([-2,-1]) == -1

def test_3():
    sol = Solution()
    assert sol.maxSubArray([-2,-1,3]) == 3

def test_4():
    sol = Solution()
    assert sol.maxSubArray([-2,1]) == 1

def test_5():
    sol = Solution()
    assert sol.maxSubArray([-1,-2]) == 1