# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from binarytree import TreeNode

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        result = []        
        queue = [(0, root)]
        while queue != []:
            level, curr = queue.pop(0)
            if level >= len(result):
                if curr is not None:
                    result.append([curr.val])
            else:
                result[level].append(curr.val)
            
            for c in [curr.left, curr.right]:
                if c is not None:
                    queue.append((level+1, c))

        for i in range(1,len(result),2):
            result[i] = result[i][::-1]

        return result

if __name__ == '__main__':

    input_list = [
        [3,9,20,None,None,15,7],
    ]

    sol = Solution()
    for inp in input_list:
        root = TreeNode.list2tree(inp)
        result = sol.zigzagLevelOrder(root)
        print(result)