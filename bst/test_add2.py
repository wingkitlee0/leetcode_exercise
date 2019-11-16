import numpy as np 
from tree import Tree

if __name__ == '__main__':
    root = None

    np.random.seed(1234)
    for i in np.random.randint(0, 100, 10):
        print(i)

        if root is None:
            root = Tree(i)
        else:
            root.addNode(i)

    print("Printing the whole tree: ")
    root.printTree()

    print("Printing the tree with level")
    root.printTreeLevel(0)

    print("Printing the tree by level")
    root.printTreeByLevel(root)


    # single node tree:
    t = Tree(0)
    t.printTreeByLevel(t)