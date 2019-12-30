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

        count = 0
        i = 0
        stack = []

        while i < n-1:
            print(i, count, stack)
            if height[i] > height[i+1]:
                print(f"append: h[{i}]:{height[i]}")
                stack.append( (i, height[i], height[i]-height[i+1]))
            if height[i] < height[i+1]:
                print(f"current: h[{i}]:{height[i]} -> h[{i+1}]:{height[i+1]}")
                while len(stack) >=1:
                    j, h, drop = stack.pop()
                    width = i-j
                    bottom = h - drop
                    print(drop, height[i+1], bottom)
                    count += width * min(drop, height[i+1]-bottom)
                    print("pop: {} -> {}".format((j, h), count))
                    if h >= height[i+1]:
                        stack.append((j, h, h-height[i+1]))
                        break

            i += 1
        return count