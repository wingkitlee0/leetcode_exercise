from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        generate all possible subsets from an list of unique integers
        """

        if nums == []:
            return []

        result = []
        curr = []
        
        def dfs(nums, start, level):
            """
            depth-first-search

            the level variable is optional for the algorithm
            """
            print("{} : {}".format(level, curr) )
            result.append(curr[:])
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(nums, start+1, level+1)
                start += 1
                curr.pop()
        dfs(nums, 0, 0)
        return result

        
if __name__ == '__main__':
    A = [4, 5, 6]
    sol = Solution()
    result = sol.subsets(A)
    print(result)