# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST_0(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        if root.left or root.right :
            if root.val < L and root.right:
                return self.rangeSumBST(root.right, L, R)
            elif root.val >= R and root.left:
                return self.rangeSumBST(root.left, L, R)
            else:
                return self.rangeSumBST(root.left, L, root.val) \
                        + self.rangeSumBST(root.right, root.val, R) \
                        + root.val
        else:
            if root.val >= L and root.val < R:
                return root.val 

    def rangeSumBST_1(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        total = 0
        
        
        if root is None:
            return 0

        print("find [", L, ",", R, "] at ", root.val)
        if root.val >= L and root.val <= R:
           total += root.val
           print("---C", total, root.val)
        
        if root.right:
            if root.val < L:
                total += self.rangeSumBST(root.right, L, R)
            else:
                total += self.rangeSumBST(root.right, root.val, R)
            print("---R", total, root.val)
        if root.left:
            if root.val > R:
                total += self.rangeSumBST(root.left, L, R)
            else:
                total += self.rangeSumBST(root.left, L, root.val)
            print("---L", total, root.val)
        return total    

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        total = 0
        
        
        if root is None:
            return 0

        print("find [", L, ",", R, "] at ", root.val)
        if root.val >= L and root.val <= R:
           total += root.val
           print("---C", total, root.val)
        
        if root.right:
            total += self.rangeSumBST(root.right, max(root.val, L), R)
            print("---R", total, root.val)
        if root.left:
            total += self.rangeSumBST(root.left, L, min(R, root.val))
            print("---L", total, root.val)
        return total

if __name__=='__main__':
    from tree import Tree

    this = Tree(5)
    this.left = Tree(3)
    this.left.left = Tree(1)
    this.left.right = Tree(4)
    this.right = Tree(8)
    this.right.right = Tree(10)
    this.right.left = Tree(6)

    this.printTree()

    sol = Solution()

    print(sol.rangeSumBST(this, 4, 7))

    print("test 2")

    this = Tree(15)
    this.left = Tree(9)
    this.left.left = Tree(7)
    this.left.left.left = Tree(5)
    this.left.right = Tree(13)
    this.left.right.left = Tree(11)
    this.right = Tree(21)
    this.right.left = Tree(19)
    this.right.right = Tree(23)
    this.right.left.left = Tree(17)

    this.printTree()
    print(sol.rangeSumBST(this, 21, 23))