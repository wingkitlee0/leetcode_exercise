class Tree:
    """A basic binary search tree
    """
    def __init__(self, val=None, compare=lambda x, y: y>=x):
        self.val = val
        self.left = None
        self.right = None
        self.compare = compare

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()

    def addNode(self, val):
        #print("compare", self.val, val, 'R' if self.compare(self.val, val) else 'L')
        if self.compare(self.val, val):
            if self.right is None:
                self.right = Tree(val=val, compare=self.compare)
            else:
                self.right.addNode(val)
        else:
            if self.left is None:
                self.left = Tree(val=val, compare=self.compare)
            else:
                self.left.addNode(val=val)

    def printTreeLevel(self, level):
        print(level, " : ", self.val)
        if self.left:
            self.left.printTreeLevel(level+1)
        if self.right:
            self.right.printTreeLevel(level+1)

    def del_max(self):
        if self.right is None:
            # remove the head when there is no right child
            return self.left
        elif self.right.right is None:
            # 
            self.right = self.right.left
            return self
        else:
            # remove the max in the right child tree
            self.right.del_max()
            return self

    def find_max(self):
        if self.right is None:
            return self.val
        elif self.right.right is None:
            return self.right.val
        else:
            return self.right.find_max()