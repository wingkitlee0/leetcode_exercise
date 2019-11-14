# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from binarytree import TreeNode

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:


        def dfs(root: TreeNode) -> (int, bool):
            """
            return the maxPathSum and a bool whether the a one-sided path with root node is used

            i.e., if a parent-child path is used..
            """

            if root is None:
                return float('-Inf'), True

            if root.left is None and root.right is None:
                return root.val, True
            
            if root.left is not None:
                leftmax, leftgoodpath = dfs(root.left)
            else:
                leftmax, leftgoodpath = float('-Inf'), True

            if root.right is not None:
                rightmax, rightgoodpath = dfs(root.right)
            else:
                rightmax, rightgoodpath = float('-Inf'), True


            if leftgoodpath:
                if rightgoodpath:
                    # both goodpath
                    currmax = max(leftmax, root.val+leftmax, root.val+rightmax, rightmax, root.val)

                    if leftmax == currmax or rightmax == currmax:
                        if root.val+leftmax+rightmax > currmax:
                            currmax = root.val+leftmax+rightmax
                        goodpath = False
                    else:
                        if root.val+leftmax+rightmax > currmax:
                            currmax = root.val+leftmax+rightmax
                            goodpath = False
                        else:
                            goodpath = True
                else:
                    # only left child tree is goodpath
                    currmax = max(leftmax, root.val+leftmax, rightmax, root.val)
                    goodpath = True
            else:
                if rightgoodpath:
                    # only right child tree is goodpath
                    currmax = max(leftmax, root.val+rightmax, rightmax, root.val)
                    goodpath = True
                else:
                    # both left and right child trees are not goodpath
                    currmax = max(leftmax, rightmax, root.val)
                    goodpath = False
            
            print(root.val, currmax, leftmax, rightmax, goodpath)
            return currmax, goodpath

        _max, _ = dfs(root)
        return _max

if __name__ == '__main__':
    input_list = [
        [1,2,3],
        [-10, 9, 20, None, None, 15, 7],
        [-2, -1],
        [1,-2,-3,1,3,-2,None,-1],
        [0, 1, 1],
        [5,4,8,11,None,13,4,7,2,None,None,None,1]
    ]

    sol = Solution()
    for inp in input_list:
        tree = TreeNode.list2tree(inp)
        TreeNode.printTree_bfs(tree)

        result = sol.maxPathSum(tree)
        print("{} : {}".format(inp, result))
        