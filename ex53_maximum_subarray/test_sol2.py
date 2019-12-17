from typing import List

class Solution:
    def maxSubnumsay(self, nums: List[int]) -> int:

        curr = nums[0]
        maximum = curr
        jmax = 1
        i = 0
        for j in range(1, len(nums)):
            #print(i, j, curr)
            if curr > 0:
                curr += nums[j]
            else:
                curr = nums[j]
                i = j

            if curr >= maximum:
                maximum = curr
                jmax = j

        jmax += 1

        #return maximum, i, jmax
        return maximum


def test_1():
    sol = Solution()
    assert sol.maxSubnumsay([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_2():
    sol = Solution()
    assert sol.maxSubnumsay([-2,-1]) == -1

def test_3():
    sol = Solution()
    assert sol.maxSubnumsay([-2,-1,3]) == 3

def test_4():
    sol = Solution()
    assert sol.maxSubnumsay([-2,1]) == 1

def test_5():
    sol = Solution()
    assert sol.maxSubnumsay([-1,-2]) == -1