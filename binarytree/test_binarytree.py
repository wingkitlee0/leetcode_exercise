import pytest

from binarytree import TreeNode


class TestBinaryTree:
    def test_binarytree_0001(self):
        tree = TreeNode.from_list([0, None, 2])

        assert tree.val == 0
        assert tree.left is None
        assert tree.right.val == 2
        assert tree.right == TreeNode(2)

    def test_binarytree_0002(self):
        tree = TreeNode.from_list(
            [1, None, 0, 0, 1],
        )

        assert tree.val == 1
        assert tree.left is None
        assert tree.right.val == 0
        assert tree.right.left == TreeNode(0)
        assert tree.right.right == TreeNode(1)

    def test_binarytree_0003(self):
        tree = TreeNode.from_list(
            [1, 2, 3, 4, None, 5, 6],
        )

        assert tree.val == 1
        assert tree.left.val == 2
        assert tree.right.val == 3
        assert tree.left.left == TreeNode(4)
        assert tree.left.right is None
        assert tree.right.left == TreeNode(5)
        assert tree.right.right == TreeNode(6)

    def test_binarytree_0004(self):
        tree = TreeNode.from_list(
            [1, 2, None, 4, None, 5, 6],
        )

        assert tree.val == 1
        assert tree.left.val == 2
        assert tree.right is None
        assert tree.left.left.val == 4
        assert tree.left.right is None
        assert tree.left.left.left == TreeNode(5)
        assert tree.left.left.right == TreeNode(6)

    def test_binarytree_0010(self):

        with pytest.raises(TypeError):
            TreeNode.from_list(None)

        assert TreeNode.from_list([]) is None
        assert TreeNode.from_list([None]) is None
        assert TreeNode.from_list([1]) == TreeNode(1)
