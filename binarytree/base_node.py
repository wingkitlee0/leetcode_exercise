from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any, Generic, List, Optional, Type, TypeVar

T = TypeVar("T", bound="BaseNode")


@dataclass
class BaseNode(Generic[T]):
    """ABC for a node"""

    val: Any
    left: Optional[T] = None
    right: Optional[T] = None

    def __eq__(self, o) -> bool:
        return (self.val == o.val) & (self.left == o.left) & (self.right == o.right)

    def __str__(self) -> str:
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None

        return f"{type(self).__name__}(V={self.val}, L={left}, R={right})"

    @classmethod
    def from_list(cls: Type[T], lst: List[Any]) -> Optional[T]:
        """Convert a list into a binary tree"""
        print(f"Converting a list to a {cls.__name__}")

        if len(lst) == 0:
            return None
        if lst[0] is None:
            return None
        if len(lst) == 1:
            return cls(lst[0])

        root = cls(lst[0])

        i = 1  #: index of the input list
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
            if i >= len(lst):
                break
            x = lst[i]
            if x is not None:
                curr.right = cls(x)
                queue.append(curr.right)

            i += 1
        return root
