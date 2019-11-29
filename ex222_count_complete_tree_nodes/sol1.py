# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from binarytree import TreeNode

class Solution:
    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        cnt = 0
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr is None:
                break
            else:
                cnt += 1

            for node in [curr.left, curr.right]:
                queue.append(node)

        return cnt

if __name__ == '__main__':

    input_list = [
        [1,2,3,4,5,6], # 6
        [1,2,3,4,5], # 5
        [1,2,3], # 3
        [],
        [1]
    ]

    sol = Solution()
    for inp in input_list:
        tree = TreeNode.list2tree(inp)
        result = sol.countNodes(tree)
        print(result)