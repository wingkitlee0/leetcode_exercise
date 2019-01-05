# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printNodes(node):
    print(node.val)
    while node.next is not None:
        node = node.next
        print(node.val)


class Solution:
    def swapNext(self, node0):
        """swap with the next node"""
        if node0.next is not None:
            node1 = node0.next
            node2 = node1.next
            # swap
            node0.next = node2
            node1.next = node0
            return node1
        else:
            return node0

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            head = self.swapNext(head) # swap the first pair
            current = head # pointer to the current pair, to be updated
            while current.next is not None and current.next.next is not None:
                current.next.next = self.swapNext(current.next.next)
                current = current.next.next # move forward
            
            return head
        

if __name__ == "__main__":
    # stupid way to create a list
    myList = ListNode(1)
    myList.next = ListNode(2)
    myList.next.next = ListNode(3)
    myList.next.next.next = ListNode(4)
    myList.next.next.next.next = ListNode(5)
    myList.next.next.next.next.next = ListNode(6)
    myList.next.next.next.next.next.next = ListNode(7)
    myList.next.next.next.next.next.next.next = ListNode(8)
    
    sol = Solution()

    printNodes(myList)

    import copy
    myList2 = copy.deepcopy(myList)
    print("\n---")
    
    myList = sol.swapNext(myList)
    current = myList
    while current.next is not None and current.next.next is not None:
        current.next.next = sol.swapNext(current.next.next)
        current = current.next.next
    printNodes(myList)

    print("\n---test----")
    myList2 = sol.swapPairs(myList2)
    printNodes(myList2)