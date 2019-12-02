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
            


        
            

            
        

if __name__ == '__main__':

    input_list = [
        [1,2,3,4,5],
        [1],
        [1,2]
    ]

    for inp in input_list:
        listnode = ListNode.list2node(inp)
        print(listnode)
        