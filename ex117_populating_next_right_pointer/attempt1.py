from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from binarytree import BaseMixin, BaseNode


@dataclass(unsafe_hash=True)
class Node(BaseMixin, BaseNode):
    next: Optional[Node] = None

    def __str__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        next = self.next.val if self.next else None

        return f"Node(v={self.val}, l={left}, r={right}, n={next})"


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: Node) -> Node:

        if root is None:
            return None

        print(f"Connecting {type(root).__name__}({root.val})")

        self.make_connection(root=root)

        _ = self.connect(root.left)
        _ = self.connect(root.right)

        return root

    def make_connection(self, root: Node) -> Node:
        """Assuming root.next has been assigned (can be None)"""

        if root is None:
            return root

        if root.left is None and root.right is None:
            return root

        if root.next is None:
            # only deal with two children
            if root.left is not None and root.right is not None:
                root.left.next = root.right
        else:
            # 4 cases
            if root.left is None:
                if root.right is not None:
                    # find the next pointer for right
                    root.right.next = self.find_left_most_pointer(root.next)
            else:
                if root.right is None:
                    root.left.next = self.find_left_most_pointer(root.next)
                else:
                    root.left.next = root.right
                    root.right.next = self.find_left_most_pointer(root.next)
        return root

    def find_left_most_pointer(self, root: Node) -> Optional[Node]:
        """Return the left most child"""
        if root is not None:
            if root.left is not None:
                return root.left
            elif root.right is not None:
                return root.right
            else:
                # root has no child
                return self.find_left_most_pointer(root=root.next)
        else:
            return None


def main():
    # tree = from_list([1, 2, 3, 4, 5, None, 7], node=Node)
    tree = Node.from_list([1, 2, 3, 4, 5, None, 7])
    tree.printTree(print_children=True)

    print("==")
    tree.print()

    sol = Solution()
    tree = sol.connect(tree)

    print("==")
    tree.print()

    print("==")
    result = tree.bfs_with_none()
    print([r[1].val if r[1] else None for r in result])


if __name__ == "__main__":
    main()
