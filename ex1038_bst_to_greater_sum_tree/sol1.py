# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Example:
    Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
"""

from binarytree import TreeNode
import copy

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #root.printTree_bfs()

        curr = copy.copy(root)

        def dfs(root, greater_sum=0):
            if root:
                if root.right:
                    greater_sum = dfs(root.right, greater_sum)
                #greater_sum += root.val
                
                root.val += greater_sum
                greater_sum = root.val
                #print(root.val, greater_sum)
                if root.left:
                    greater_sum = dfs(root.left, greater_sum)
                return greater_sum
            else:
                return 0
        
        dfs(curr, greater_sum=0)

        return curr

if __name__ == '__main__':

    input_list = [
        [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    ]

    sol = Solution()

    for inp in input_list:
        tree = TreeNode.list2tree(inp)
        tree.printTree()

        result = sol.bstToGst(tree)
        result.printTree()
