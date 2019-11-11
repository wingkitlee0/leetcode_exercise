from __future__ import annotations
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def printTree(root: TreeNode):
        if root.left:
            TreeNode.printTree(root.left)
        print(root.val)
        if root.right:
            TreeNode.printTree(root.right)
        
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

        root = TreeNode(inp.pop(0))
        

        queue = [root]
        while queue != [] and inp != []:
            curr = queue.pop(0)
            if (x:= inp.pop(0)) is not None:
                curr.left = TreeNode(x)
                queue.append(curr.left)
            if (x:= inp.pop(0)) is not None:
                curr.right = TreeNode(x)
                queue.append(curr.right)


        return root

if __name__ == '__main__':

    input_list = [
        [0, None, 3],
        [1,None,0,0,1],
    ]

    for i, x in enumerate(input_list):
        tree = TreeNode.list2tree(x)
        print("=============={}==============".format(i))
        TreeNode.printTree(tree)

