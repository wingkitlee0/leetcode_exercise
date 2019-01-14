class Tree:
    """A basic binary search tree
    """
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()

    def addNode(self, val):
        if val >= self.val:
            if self.right is None:
                self.right = Tree(val=val)
            else:
                self.right.addNode(val)
        else:
            if self.left is None:
                self.left = Tree(val=val)
            else:
                self.left.addNode(val=val)

