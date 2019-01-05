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
        node1 = node0.next
        node2 = node1.next
        # swap
        node0.next = node2
        node1.next = node0
        return node1

    def getSecondLastNode(self, node):
        if node is not None and node.next is not None:
            print(node)
            n0 = node
            n2 = node.next.next
            while n2.next.next is not None:
                n0 = n2
                n2 = n0.next.next
            return n0, n2

    def swapNext2(self, n0, n2):
        """
        Swapping the first two nodes, and attach back the third:
        n0->n1->n2 --> n1->n0->n2
        return the new head (n1)
        """
        n1 = n0.next
        # swap
        n0.next = n2
        n1.next = n0
        return n1

if __name__ == "__main__":
    # stupid way to create a list
    myList = ListNode(1)
    myList.next = ListNode(2)
    myList.next.next = ListNode(3)
    myList.next.next.next = ListNode(4)
    myList.next.next.next.next = ListNode(5)
    myList.next.next.next.next.next = ListNode(6)
    
    printNodes(myList)

    sol = Solution()
    myList2 = sol.swapNext(myList)

    printNodes(myList2)

    print("---")
    n0, n2 = sol.getSecondLastNode(myList2)
    printNodes(n2)
    print("swapping")
    n2_ = sol.swapNext(n2)
    printNodes(n2_)

    print("\n---")
    n0, n2 = sol.getSecondLastNode(myList)
    printNodes(n2)
    print("swapping")
    n0_ = sol.swapNext2(n0, n2)
    printNodes(n0_)