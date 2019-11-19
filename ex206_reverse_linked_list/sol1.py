# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def print_values(node):
        if node is None:
            print("None")
        while node:
            print(node.val, end=" ")
            if node.next:
                node = node.next
            else:
                break
        print()

    @staticmethod
    def list2nodes(lst):
        if lst is None or lst == []:
            return None
        head = ListNode(inp.pop(0))
        node = head
        while inp != []:
            node.next = ListNode(inp.pop(0))
            node = node.next
        return head

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        recursive version
        """
        if head is None:
            return None

        def append(node, head):
            """
            return new_head, new_tail
            """
            node.next = None

            if head is None:
                return node, node
            else:
                if head.next is None:
                    head.next = node
                    return head, node
                else:
                    new_head, tmp_tail = append(head, head.next)
                    tmp_tail.next = node
                    return new_head, node

        new_head, _ = append(head, head.next)
        return new_head

if __name__ == '__main__':

    inp = [1, 2, 3, 4]

    head = ListNode.list2nodes(inp)    
    ListNode.print_values(head)

    sol = Solution()
    result = sol.reverseList(head)
    
    ListNode.print_values(result)