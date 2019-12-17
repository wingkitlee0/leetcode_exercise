# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from binarytree import TreeNode
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        leftmost = None; 
        queue = deque()
        queue.append( (root, 0))
        leftmost = root.val; lastlevel = 0

        while queue:
            
            curr, level = queue.popleft()

            print(curr.val, level)

            if level > lastlevel:
                leftmost = curr.val
                lastlevel = level

            if curr is not None:
                for child in [curr.left, curr.right]:
                    if child is not None:
                        queue.append((child, level+1))

        #print("leftmost list = {}".format(leftmost_list))

        return leftmost

    def findBottomLeftValue_old(self, root: TreeNode) -> int:

        leftmost_list = []
        #leftmost = None; lastlevel = 0

        queue = deque()
        queue.append( (root, 0))
        leftmost = roo
        leftmost_list.append(root.val)
        while queue:
            
            curr, level = queue.popleft()

            print(curr.val, level)

            if level >= len(leftmost_list):
                leftmost_list.append(curr.val)

            if curr is not None:
                for child in [curr.left, curr.right]:
                    if child is not None:
                        queue.append((child, level+1))

        print("leftmost list = {}".format(leftmost_list))

        return leftmost_list[-1]


if __name__ == '__main__':
    from binarytree import TreeNode

    input_list = [
        [1,2,3,4,None,5,6,None,None,None,None,7,None],
    ]

    sol = Solution()

    for inp in input_list:
        tree = TreeNode.list2tree(inp)
        result = sol.findBottomLeftValue(tree)
        print("{} : {}".format(inp, result))
    
    