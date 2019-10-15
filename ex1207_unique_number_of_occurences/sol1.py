from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = dict()

        for x in arr:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

        r = dict()
        for k, v in counts.items():
            if v in r:
                return False
            else:
                r[v] = 1
        
        return True


if __name__ == '__main__':

    arrs = [[1,2,2,1,1,3],
            [1,2],
            [-3,0,1,-3,1,1,1,-3,10,0]
            ]
    sol = Solution()

    for i, arr in enumerate(arrs):
        result = sol.uniqueOccurrences(arr)
        print(i, result)
