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

    def printTreeLevel(self, level):
        print(level, " : ", self.val)
        if self.left:
            self.left.printTreeLevel(level+1)
        if self.right:
            self.right.printTreeLevel(level+1)

    def printTreeByLevel(self, root):

        if root is None:
            print("Root is None. Nothing to print!")

        frontier = [(0, root)]
        result = []
        
        while frontier != []:
            
            node_lvl, node = frontier.pop(0)
            result.append( (node_lvl, node.val) )

            for child in [node.left, node.right]:
                if child:
                    frontier.append( (node_lvl+1, child))
            

        for x in result:
            print("{} : {}".format(x[0], x[1]) )


