from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        # create dictionary
        loc = dict()
        for i, x in enumerate(nums):
            if x in loc:
                loc[x].append(i)
            else:
                loc[x] = [i]

        for i in range(n):
            x = nums[i]
            for j in range(n):
                if j != i:
                    y = nums[j]

                    for k in range(n):
                        if k != j and k != i:
                            z = nums[k]
                            w = target - x - y -z

                            if w in loc:
                                for l in loc[w]:
                                    print([i, j, k, l])
                            
                            


        return []

if __name__ == '__main__':
    A = [1, 0, -1, 0, -2, 2]
    target = 0

    sol = Solution()
    result = sol.fourSum(A, target)
    print(result)

