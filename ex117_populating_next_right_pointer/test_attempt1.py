import pytest
from ex117_populating_next_right_pointer.main import Node, Solution

class TestNextPointer:

    def test_0001(self):
        tree = Node.from_list([1, 2, 3, 4, 5, None, 7])

        solution = Solution()
        solution.connect(root=tree)

        assert tree.next is None
        assert tree.left.next == tree.right
        assert tree.right.next is None
        assert tree.left.left.next == tree.left.right

    def test_0002(self):
        tree = Node.from_list([1,2,3,4,5,None,6,7,None,None,None,None,8])

        solution = Solution()
        solution.connect(root=tree)

        assert tree.val == 1
        assert tree.right.val == 3
        assert tree.right.right.val == 6
        assert tree.right.right.right.val == 8
        assert tree.left.left.next == tree.left.right
        assert tree.left.right.next == tree.right.right
        assert tree.left.left.left.next == tree.right.right.right # interesting!

    def test_0003(self):
        tree = Node.from_list([ 1,2,3,4,None, None, 5, 6, None, None,7])

        solution = Solution()
        solution.connect(root=tree)

        assert tree.val == 1
        assert tree.right.val == 3
        assert tree.right.right.val == 5
        assert tree.right.right.right.val == 7
        assert tree.left.left.next == tree.right.right
        assert tree.left.left.left.next == tree.right.right.right