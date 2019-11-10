from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        4-sum

        simple extension of two-sum: create a dictionary first and loop through the whole array.

        this leads to complexity of O(n^3) ...
        """
        n = len(nums)

        if nums == []:
            return []

        nums = sorted(nums)
        # create dictionary
        loc = dict()
        for i, x in enumerate(nums):
            loc[x] = i

        result = set()
        for i in range(n):
            x = nums[i]
            for j in range(i+1, n):
                y = nums[j]

                for k in range(j+1, n):
                    z = nums[k]
                    w = target - x - y -z

                    if w in loc:
                        if loc[w] > k:
                            #result.append([x, y, z, w])
                            #result.add(tuple(sorted([x, y, z, w])))
                            result.add((x, y, z, w))

        return [list(l) for l in result]
        #return [list(l) for l in set(tuple(r) for r in result)]

if __name__ == '__main__':
    #A = [1, 0, -1, 0, -2, 2]
    A = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0

    sol = Solution()
    result = sol.fourSum(A, target)

    if len(result) > 1:
        for r in result:
            print(r)

