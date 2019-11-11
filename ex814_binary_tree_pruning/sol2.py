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
        """
        prune the tree recursively!
        """

        if root is None:
            return None
        
        if root.left is not None:
            root.left = self.pruneTree(root.left)
        
        if root.right is not None:
            root.right = self.pruneTree(root.right)

        if root.left is None and root.right is None:
            if root.val == 0:
                return None
            else:
                return root

        return root

    def pruneTree_stack(self, root: TreeNode) -> TreeNode:
        """
        prune the tree recursively!
        """

        def pruneLeave(r: TreeNode) -> TreeNode:
            if r is None:
                return None
            else:
                if r.left is None and r.right is None:
                    if r.val == 0:
                        return None
                    else:
                        return r

        if root is None:
            return None
        
        stack = [root]

        while stack != []:
            curr = stack.pop()

            if curr is not None:
                if curr.left is not None:
                    curr.left = pruneLeave(curr.left)
                    stack.append(curr.left)
                if curr.right is not None:
                    curr.right = pruneLeave(curr.right)
                    stack.append(curr.right)
        
                if curr.left is None and curr.right is None:
                    if curr.val == 0:
                        curr = None

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

    
        #tree_ = sol.pruneTree(tree)
        tree_ = sol.pruneTree_stack(tree)
        TreeNode.printTree_bfs(tree_)
                