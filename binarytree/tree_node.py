# treenode
from dataclasses import dataclass

from binarytree import BaseMixin, BaseNode


@dataclass(unsafe_hash=True)
class TreeNode(BaseMixin, BaseNode):
    pass


if __name__ == "__main__":

    input_list = [
        [0, None, 3],
        [1, None, 0, 0, 1],
    ]

    for i, lst in enumerate(input_list):
        tree = TreeNode.from_list(lst)

        print(f"=============={i}==============")
        if tree is not None:
            tree.printTree_bfs2()
        else:
            print("Tree is None!")
