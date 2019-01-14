import numpy as np 
from tree import Tree

if __name__ == '__main__':
    root = Tree(1)

    np.random.seed(1234)
    for i in np.random.randint(0, 100, 10):
        print(i)
        root.addNode(i)

    print("Printing the whole tree: ")
    root.printTree()