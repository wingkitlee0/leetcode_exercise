import numpy as np 
from tree import Tree

def deleteNode(root, key):
    if key == root.val:
        pass

def list2Tree(lst):
    if len(lst) == 0:
        return None
    else:
        root = Tree(lst[0])
        if len(lst) > 1:
            for i in lst[1:]:
                root.addNode(i)
        return root


if __name__ == '__main__':

    root = list2Tree([5,3,6,2,4,7])

    print("Printing the whole tree: ")
    root.printTreeLevel(0)