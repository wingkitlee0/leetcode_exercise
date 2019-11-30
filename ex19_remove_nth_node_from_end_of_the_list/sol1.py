# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def list2node(lst_):
        lst = lst_.copy()

        if len(lst) == 0:
            return None
        if len(lst) == 1:
            return ListNode(lst[0])

        root = ListNode(lst.pop(0))
        curr = root
        while lst != []:
            val = lst.pop(0)
            curr.next = ListNode(val)
            curr = curr.next
        
        return root

    @staticmethod
    def print(root):
        if root is None:
            return
        print(root.val)
        ListNode.print(root.next)

    def __str__(self):
        def dfs(root, res):
            if not root:
                return
            res.append(root.val)
            if root.next is not None:
                dfs(root.next, res)
        res = []
        dfs(self, res)
        return "->".join([str(r) for r in res])
            


        
            
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        create a front pointer that is n steps ahead
        """

        front = head
        i = 0
        while i < n and front is not None:
            front = front.next
            i += 1

        print(front)

        if not front and i==n:
            return head.next

        curr = head
        while front.next is not None:
            curr = curr.next
            front = front.next

        print(curr)
        print(front)

        # remove curr.next
        temp = curr.next.next
        curr.next = temp

        return head       

            
        

if __name__ == '__main__':

    input_list = [
        ([1,2,3,4,5], 2),
        ([1], 1),
        ([1,2], 2)
    ]

    sol = Solution()

    for inp in input_list:
        listnode = ListNode.list2node(inp[0])
        print(listnode)
        result = sol.removeNthFromEnd(listnode, inp[1])
        print(result)