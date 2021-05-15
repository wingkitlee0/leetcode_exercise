from __future__ import annotations

from abc import ABC
from collections import deque
from dataclasses import dataclass, field
from typing import Any, List, Optional

from binarytree.base_mixin import BaseMixin


@dataclass(unsafe_hash=True)
class BaseNode(ABC):
    """ABC for a node"""
    val: Any
    left: Optional[BaseNode] = None
    right: Optional[BaseNode] = None

    def __eq__(self, o) -> bool:
        return (self.val == o.val) & (self.left == o.left) & (self.right == o.right)

    def __str__(self) -> str:
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None

        return f"{type(self).__name__}(V={self.val}, L={left}, R={right})"

    @classmethod
    def from_list(cls, lst: List[Any]) -> Optional[BaseNode]:
        """Convert a list into a binary tree"""
        print(f"Converting a list to a {cls.__name__}")

        if len(lst) == 0:
            return None
        if lst[0] is None:
            return None
        if len(lst) == 1:
            return cls(lst[0])

        root = cls(lst[0])

        i = 1 #: index of the input list
        queue = deque([root])

        # Construct the tree in a BFS way
        # consume the input queue one by one
        while len(queue) > 0 and i < len(lst):
            curr = queue.popleft()
            x = lst[i]

            # do nothing if None, as the left child is already None
            if x is not None:
                curr.left = cls(x)
                queue.append(curr.left)

            i += 1
            x = lst[i]
            if x is not None:
                curr.right = cls(x)
                queue.append(curr.right)

            i += 1
        return root


@dataclass(unsafe_hash=True)
class TreeNode(BaseNode, BaseMixin):
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
