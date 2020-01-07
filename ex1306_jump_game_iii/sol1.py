"""
Leetcode ex1306
"""

from typing import List
from collections import deque

class Solution:
    """Solution class"""
    def canReach(self, arr: List[int], start: int) -> bool:
        """canReach"""
        queue = deque()
        queue.append(start)
        seen = set()

        while queue:
            idx = queue.pop()
            print(f"current index, value = {idx}, {arr[idx]}")
            seen.add(idx)

            if arr[idx] == 0:
                return True   
            if 0 <= (new_idx:= idx + arr[idx]) < len(arr) and new_idx not in seen:
                queue.append(new_idx)
            if 0 <= (new_idx:= idx - arr[idx]) < len(arr) and new_idx not in seen:
                queue.append(new_idx)

        return False

def main():
    """main"""
    input_list = [
        [[4, 2, 3, 0, 3, 1, 2], 5], # true
        [[4, 2, 3, 0, 3, 1, 2], 0], # true
        [[3, 0, 2, 1, 2], 2], # false
        [[0, 1], 1], # true
    ]

    sol = Solution()
    for input_ in input_list:
        result = sol.canReach(*input_)
        print(f"{input_[0]}, {input_[1]} -> {result}")
        print("-"*10)

if __name__ == "__main__":
    main()
