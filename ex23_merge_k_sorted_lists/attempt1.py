# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List

from list_node import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)

    @classmethod
    def merge_two_lists(cls, list1: ListNode, list2: ListNode) -> ListNode:

        a, b = (list1, list2) if list1 < list2 else (list2, list1)
        root = a

        while a and b:
            print(f"Comparing {a} and {b}")
            if a < b:
                print(f"{a} < {b}")
                anext = a.next
                if anext is not None:
                    print("a.next is not None")
                    if anext < b:
                        # print(f"a.next < {b}")
                        a = a.next
                        continue
                    else:
                        print(f"Inserting {b}. Advance a")
                        bnext = b.next
                        if bnext:
                            while bnext.next and bnext.next < anext:
                                print(f"Examining {bnext.next}")
                                bnext = bnext.next
                            print(f"a={a}")
                            print(f"b={b}")
                            print(f"anext={anext}")
                            print(f"bnext={bnext}")

                            a.next, b, bnext.next = b, bnext.next, anext
                        else:
                            print(f"a={a}")
                            print(f"b={b}")
                            print(f"anext={anext}")
                            print(f"bnext={bnext}")
                            a.next, b.next = b, anext
                        a = a.next
                else:
                    a.next, b = b, b.next
                    break
            else:
                a = a.next

        return root
