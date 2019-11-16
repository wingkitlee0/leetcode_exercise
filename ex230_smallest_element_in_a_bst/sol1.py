# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        stack = []
        curr = root
        
        cnt = 0
        while True:

            if curr is not None:
                stack.append(curr)
                curr = curr.left
            
            elif stack:

                curr = stack.pop()
                
                print(curr.val, cnt)
                if cnt == k+1:
                    return curr.val

                cnt += 1
                curr = curr.right
            else:
                break

        return None


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

    result = sol.kthSmallest(tree, k=1)
    print(result)

    