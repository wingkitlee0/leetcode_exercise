from typing import List, Tuple

"""
Bruce-force solution

Time complexity O(nm) where n, m are the len and max of the height array
"""

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if n < 3:
            return 0
        max_height = max(height)
        
        istart, iend = self.find_new_ends(height, 0, n-1)
        print(istart, iend)
    
        count = 0
        level = 1
        while iend > istart and level <= max_height:  
            print("{}: {}".format(level, height[istart:iend+1]))
            istart, iend = self.find_new_ends(height, istart, iend) 
            for i in range(istart, iend+1):
                if height[i] == 0:
                    height[i] = 1
                    count += 1
                height[i] -= 1
            level += 1
            
        return count

    def find_new_ends(self, height: List[int], istart: int, iend: int) -> Tuple[int, int]:
        while height[istart] == 0:
            istart += 1
        while height[iend] == 0:
            iend -= 1
        return istart, iend