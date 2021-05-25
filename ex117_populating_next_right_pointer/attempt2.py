from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Optional

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

        def dfs(node, rnodes, level):
            if node is None:
                return rnodes

            print(f"DFS( ({node.val}), {[n.val for n in rnodes]}, {level})")

            if len(rnodes) > 0:
                next_node = rnodes.pop()
                print(f"Assigning ({node.val})->({next_node.val})")
                node.next = next_node

            if node.right is None and node.left is None:
                print(f"({node.val}) has no leave. Returns [{node.val}]")
                rnodes.append(node)
                return rnodes

            rnodes = dfs(node.right, rnodes, level + 1)
            rnodes = dfs(node.left, rnodes, level + 1)
            rnodes.append(node)
            return rnodes

        dfs(root, [], level=0)

        return root


def main():
    # tree = from_list([1, 2, 3, 4, 5, None, 7], node=Node)
    tree = Node.from_list(
        [1, 2, 3, 4, None, None, 5, 6, 7, 8, 9, None, None, None, 10, None, None, 11]
    )
    tree.printTree(print_children=True)

    print("==")
    tree.print()

    sol = Solution()
    tree = sol.connect(tree)

    print("==")
    tree.print()

    # print("==")
    # result = tree.bfs_with_none()
    # print([r[1].val if r[1] else None for r in result])


if __name__ == "__main__":
    main()
