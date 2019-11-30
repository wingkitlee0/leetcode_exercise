# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from binarytree import TreeNode

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        def dfs(tree, val):
            if tree is None:
                pass

            if val < tree.val:
                if tree.left:
                    dfs(tree.left, val)
                else:
                    tree.left = TreeNode(val)
            if val > tree.val:
                if tree.right:
                    dfs(tree.right, val)
                else:
                    tree.right = TreeNode(val)
                
        dfs(root, val)
        return root

if __name__ == '__main__':

    input_list = [
        (5, [4,2,7,1,3])
    ]

    sol = Solution()

    for inp in input_list:
        tree = TreeNode.list2tree(inp[1])
        new_tree = sol.insertIntoBST(tree, inp[0])
        new_tree.printTree_bfs()
        

