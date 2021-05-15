from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING, Any, Deque, List, Protocol, Tuple

from binarytree.base_node import BaseNode

if TYPE_CHECKING:
    _Base = BaseNode
else:
    _Base = object


class HasTwoChildren(Protocol):
    @property
    def left(self) -> HasTwoChildren:
        ...

    @property
    def right(self) -> HasTwoChildren:
        ...

    @property
    def val(self) -> Any:
        ...


class BaseMixin(_Base):
    def print(self):
        """Print each node using __str__()"""
        if self.left:
            self.left.print()
        print(self)
        if self.right:
            self.right.print()

    def printTree(self, print_children: bool = False):
        if self.left:
            self.left.printTree(print_children=print_children)
        if print_children:
            left_val = self.left.val if self.left else None
            right_val = self.right.val if self.right else None
            print(f"{self.val}: ({left_val}, {right_val})")
        else:
            print(self.val)
        if self.right:
            self.right.printTree(print_children=print_children)

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
        """Print the tree (BFS way)"""

        queue: Deque[Tuple[int, _Base]] = deque([(0, self)])
        while queue:
            level, curr = queue.popleft()

            print("{} : {}".format(level, curr.val))
            for child in [curr.left, curr.right]:
                if child is not None:
                    queue.append((level + 1, child))

    def bfs(self: HasTwoChildren) -> List[Tuple[int, HasTwoChildren]]:
        """Traversal of the tree by BFS"""
        frontier = deque([(0, self)])
        result = []

        while frontier:
            node_lvl, node = frontier.popleft()  # this is a queue
            result.append((node_lvl, node.val))

            for child in [node.left, node.right]:
                if child:
                    frontier.append((node_lvl + 1, child))

        return result
