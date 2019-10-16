from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        if nums == []:
            return []

        # create dictionary
        loc = dict()
        for i, x in enumerate(nums):
            #if x in loc:
            #    loc[x].append(i)
            #else:
            #    loc[x] = [i]
            loc[x] = [i]

        result = []
        for i in range(n):
            x = nums[i]
            for j in range(i+1, n):
                y = nums[j]

                for k in range(j+1, n):
                    z = nums[k]
                    w = target - x - y -z

                    if w in loc and w not in [x, y, z]:
                        for l in loc[w]:
                            if l > k:
                                #print([i, j, k, l])
                                #print([x, y, z, w])
                                result.append([x, y, z, w])
        #return result
        return [list(l) for l in set(tuple(r) for r in result)]

if __name__ == '__main__':
    #A = [1, 0, -1, 0, -2, 2]
    A = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0

    sol = Solution()
    result = sol.fourSum(A, target)

    if len(result) > 1:
        for r in result:
            print(r)

