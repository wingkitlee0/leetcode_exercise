from __future__ import annotations
from typing import List
from collections import deque

class TreeMixin:
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()

    def printTree_bfs(self):

        level = 0
        queue = [(level, self)]

        while queue != []:
            level, curr = queue.pop(0)
            if curr is not None:
                print("{} : {}".format(level, curr.val))
                for child in [curr.left, curr.right]:
                    queue.append((level+1, child))
            else:
                print("{} : {}".format(level, None))

    def printTree_bfs2(self):

        level = 0
        queue = deque()
        queue.append((level, self))

        while queue:
            level, curr = queue.popleft()
            if curr is not None:
                print("{} : {}".format(level, curr.val))
                for child in [curr.left, curr.right]:
                    queue.append((level+1, child))
            else:
                print("{} : {}".format(level, None))

class TreeNode(TreeMixin):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    @staticmethod
    def list2tree(lst: List) -> TreeNode:
        """
        convert a list into a binary tree
        """

        if len(lst) == 0:
            return None
        if len(lst) == 1:
            return TreeNode(lst[0])

        inp = lst.copy()

        root = TreeNode(inp[0])
        inp.pop(0)

        queue = [root]
        while queue != [] and inp != []:
            curr = queue.pop(0)
            x = inp.pop(0)
            if x is not None:
                curr.left = TreeNode(x)
                queue.append(curr.left)
            x = inp.pop(0)
            if x is not None:
                curr.right = TreeNode(x)
                queue.append(curr.right)

        return root

if __name__ == '__main__':

    input_list = [
        [0, None, 3],
        [1, None, 0, 0, 1],
    ]

    for i, x in enumerate(input_list):
        tree = TreeNode.list2tree(x)
        print("=============={}==============".format(i))
        tree.printTree_bfs2()
    
