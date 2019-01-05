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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current.next.next is not None:
            pass

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

    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n0 = head
        n1 = n0.next
        n2 = n1.next
        head = n1
        while n1.next is not None:
            n0.next = n2
            n1.next = n0
            n2_ = self.swapNext(n1.next)
            n0 = n2
            n1 = n0.next
        return head

if __name__ == "__main__":
    # stupid way to create a list
    myList = ListNode(1)
    myList.next = ListNode(2)
    myList.next.next = ListNode(3)
    myList.next.next.next = ListNode(4)
    myList.next.next.next.next = ListNode(5)
    myList.next.next.next.next.next = ListNode(6)
    
    printNodes(myList)
    import copy
    myList2 = copy.deepcopy(myList)

    sol = Solution()
    print("\n---")
    current = sol.swapNext(myList)
    printNodes(current)
    print("---")
    nextBatch = current.next.next
    swapped = sol.swapNext(nextBatch)
    current.next.next = swapped
    printNodes(current)
    print("---")
    nextBatch = current.next.next.next.next
    swapped = sol.swapNext(nextBatch)
    current.next.next.next.next = swapped
    printNodes(current)

    print("\n*****")
    myList2 = sol.swapNext(myList2)
    printNodes(myList2)
    current = myList2
    print("---")
    while current.next is not None and current.next.next is not None:
        nextBatch = current.next.next
        current.next.next = sol.swapNext(nextBatch)
        current = current.next.next
    printNodes(myList2)