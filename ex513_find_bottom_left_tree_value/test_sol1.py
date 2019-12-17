from sol1 import Solution
from binarytree import TreeNode

def test_1():
    sol = Solution()
    tree = TreeNode.list2tree([1,2,3])
    assert sol.findBottomLeftValue(tree) == 2

def test_2():
    sol = Solution()
    tree = TreeNode.list2tree([0])
    assert sol.findBottomLeftValue(tree) == 0