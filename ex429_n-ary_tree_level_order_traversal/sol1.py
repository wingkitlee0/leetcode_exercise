"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    @staticmethod
    def list2node(lst):
        if lst is None or lst == []:
            return None
        if len(lst) == 1:
            return Node(lst[0])

        root = Node(lst.pop(0), [])
        queue = [root]
        i = 1
        while lst != []:
            val = lst.pop(0)
            print(val, [n.val for n in queue])
            if val is None:
                curr = queue.pop(0)
                curr.children = []
            else:
                node = Node(val, [])
                curr.children.append(node)
                queue.append(node)

        return root

    def print_dfs(self, root, level=0):
        if root is None:
            pass

        print(level, root.val)
        for c in root.children:
            self.print_dfs(c, level=1)

    def print_bfs(self, root):

        queue = [(0, root)]
        while queue != []:
            level, curr = queue.pop(0)
            print(level, curr.val)
            if curr.children != []:
                for c in curr.children:
                    queue.append((level+1, c))



class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        result = []        
        queue = [(0, root)]
        while queue != []:
            level, curr = queue.pop(0)
            if level >= len(result):
                if curr is not None:
                    result.append([curr.val])
            else:
                result[level].append(curr.val)
            if curr.children != []:
                for c in curr.children:
                    if c is not None:
                        queue.append((level+1, c))

        return result
                    





if __name__ == '__main__':

    input_list = [
        [1,None,3,2,4,None,5,6],
        [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14],
        [],
    ]

    sol = Solution()
    for inp in input_list:
        tree = Node.list2node(inp)
        Node.print_dfs(tree)
        print("-------BFS-----")
        Node.print_bfs(tree)
        result = sol.levelOrder(tree)
        print(result)
        print("-------")