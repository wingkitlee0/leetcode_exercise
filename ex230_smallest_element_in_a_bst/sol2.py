# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        cnt = 0
        result = None
        def dfs(root, cnt, res):
            if root.left is not None:
                dfs(root.left, cnt, result)
            
            print(root.val, k)
            if cnt == k:
                res = root.val

            cnt += 1
            
            res.append(root.val)
            if root.right is not None:
                dfs(root.right, cnt, result)

        dfs(root, cnt, result)

        return result

    def kthSmallest_(self, root: TreeNode, k: int) -> int:

        result = []
        def dfs(root, res):
            if root.left is not None:
                dfs(root.left, res)
            print(root.val)
            res.append(root.val)
            if root.right is not None:
                dfs(root.right, res)

        dfs(root, result)

        return result[k-1]


if __name__ == '__main__':

    
    tree = TreeNode(3)
    tree.left = TreeNode(1)
    tree.right = TreeNode(4)
    tree.left.left = None
    tree.left.right = TreeNode(2)

    # [5,3,6,2,4,null,null,1]
    tree = TreeNode(5)
    tree.left = TreeNode(3)
    tree.right = TreeNode(6)
    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(4)
    tree.left.left.left = TreeNode(1)

    sol = Solution()

    result = sol.kthSmallest(tree, k=3)
    print(result)