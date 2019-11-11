# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from __future__ import annotations
import copy

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def pruneLeave(root: TreeNode) -> TreeNode:
            if root is None:
                return None
            else:
                if root.left is None and root.right is None and root.val == 0:
                    return None
                else:
                    return root
        
        level = 0
        stack = [(level, root)]
        while stack != []:
            level, curr = stack.pop()
            curr = pruneLeave(curr)
            if curr is not None:
                print(level, curr.val)
                if not curr.left and not curr.right and curr.val == 0:
                    curr = None
                else:
                    if curr.left:
                        curr.left = pruneLeave(curr.left)
                        if curr.left:
                            stack.append((level+1, curr.left))
                    if curr.right:
                        curr.right = pruneLeave(curr.right)
                        if curr.right:
                            stack.append((level+1, curr.right))
                    if not curr.left and not curr.right and curr.val == 0:
                        stack.append( (level, curr) )

        return root

if __name__ == '__main__':
    from binarytree import TreeNode

    sol = Solution()

    input_list = [
        [0, None, 3],
        [1, None, 0, 0, 1],
        [1,0,1,0,0,0,1],
    ]

    for i, x in enumerate(input_list):
        print("=============={}==============".format(x))
        tree = TreeNode.list2tree(x)
        #TreeNode.printTree(tree)

    
        tree_ = sol.pruneTree(tree)
        TreeNode.printTree_bfs(tree_)
                