# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head is None:
            return None
        if head.next is None:
            return head
        
        def append(node, head):
            if head is None:
                node.next = None
                return node
            else:
                print("calling append {}, {}".format(node.val, head.val))
                if head.next is None:
                    node.next = None
                    head.next = node
                    return head
                else:
                    tmp = head; tmp.next = None
                    new_head = append(node, head.next)
                    new_head.next = tmp
                    return new_head

        return append(ListNode(head.val), head.next)

if __name__ == '__main__':

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    sol = Solution()
    result = sol.reverseList(head)
    while result is not None:
        print(result.val)
        result = result.next