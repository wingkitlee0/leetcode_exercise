from __future__ import annotations
from typing import List

MAX_LIMIT = 100

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self) -> str:
        return f"({self.val})"

    @classmethod
    def from_list(cls, vals:List[int]) -> ListNode:

        if len(vals) == 0:
            return None
        if len(vals) == 1:
            return ListNode(val=vals[0])

        root = ListNode(val=vals[0])
        current = root
        for i in range(1, len(vals)):
            current.next = ListNode(val=vals[i])
            current = current.next

        return root

    def to_list(self) -> List[int]:
        result = []
        curr = self
        while curr:
            result.append(curr.val)
            curr = curr.next
            if len(result) > MAX_LIMIT:
                print("List length is above limit. Is it cyclic?")
                break
        return result

if __name__ == "__main__":
    root = ListNode.from_list([1, 2, 3])
    print(root.val, root.next.val, root.next.next.val)

    print(root.to_list())


