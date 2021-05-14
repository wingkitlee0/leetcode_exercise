from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Any, List, Optional


class TreeMixin:
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()

    def printTree_bfs(self):

        level = 0
        queue = [(level, self)]

        while queue != []:
            level, curr = queue.pop(0)
            if curr is not None:
                print("{} : {}".format(level, curr.val))
                for child in [curr.left, curr.right]:
                    queue.append((level + 1, child))
            else:
                print("{} : {}".format(level, None))

    def printTree_bfs2(self):

        level = 0
        queue = deque()
        queue.append((level, self))

        while queue:
            level, curr = queue.popleft()
            if curr is not None:
                print("{} : {}".format(level, curr.val))
                for child in [curr.left, curr.right]:
                    queue.append((level + 1, child))
            else:
                print("{} : {}".format(level, None))


@dataclass(unsafe_hash=True)
class TreeNode(TreeMixin):
    val: Any
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None

    def __eq__(self, o) -> bool:
        return (self.val == o.val) & (self.left == o.left) & (self.right == o.right)

    @staticmethod
    def from_list(lst: List[Any]) -> Optional[TreeNode]:
        """Convert a list into a binary tree"""

        if len(lst) == 0:
            return None
        if lst[0] is None:
            return None
        if len(lst) == 1:
            return TreeNode(lst[0])

        input = deque(lst)  # with copy

        x = input.popleft()
        root = TreeNode(x)

        queue = deque([root])

        # Construct the tree in a BFS way
        # consume the input queue one by one
        while len(queue) > 0 and len(input) > 0:
            curr = queue.popleft()
            x = input.popleft()

            # do nothing if None, as the left child is already None
            if x is not None:
                curr.left = TreeNode(x)
                queue.append(curr.left)

            x = input.popleft()
            if x is not None:
                curr.right = TreeNode(x)
                queue.append(curr.right)

        return root


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
