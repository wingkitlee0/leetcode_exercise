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

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        recursive version
        """
        ListNode.print_values(head)

        if head is None:
            return None
        if head.next is None:
            return ListNode(head.val)

        print("calling append {} to {}".format(head.val, head.next.val))
        
        tmp = self.reverseList(head.next)
        head.next.next = ListNode(head.val)

        ListNode.print_values(tmp)
        return tmp

if __name__ == '__main__':

    inp = [1, 2, 3, 4]

    head = ListNode(inp.pop(0))
    node = head
    while inp != []:
        node.next = ListNode(inp.pop(0))
        node = node.next
        
    ListNode.print_values(head)

    sol = Solution()
    result = sol.reverseList(head)
    
    ListNode.print_values(result)