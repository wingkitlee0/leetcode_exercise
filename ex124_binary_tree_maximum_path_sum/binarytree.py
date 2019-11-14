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
        else:
            print("None")
        print(root.val)
        if root.right:
            TreeNode.printTree(root.right)
        else:
            print("None")

    @staticmethod
    def printTree_bfs(root: TreeNode):

        level = 0
        queue = [(level, root)]

        while queue != []:
            level, curr = queue.pop(0)
            if curr is not None:
                print("{} : {}".format(level, curr.val))
                for child in [curr.left, curr.right]:
                    queue.append((level+1, child))
            else:
                print("{} : {}".format(level, None))

        
    @staticmethod
    def list2tree(lst: List) -> TreeNode:
        """
        convert a list into a binary tree
        """
        n = len(lst)

        if n == 0:
            return None
        if n == 1:
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
            
            if inp == []:
                break
            
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
        #TreeNode.printTree(tree)
        TreeNode.printTree_bfs(tree)
    
