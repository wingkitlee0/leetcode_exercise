from dataclasses import dataclass
from typing import Any
from binarytree import BaseNode, BaseMixin

@dataclass
class BSTNode(BaseMixin, BaseNode):

    def addNode(self, val: Any) -> None:
        if val >= self.val:
            if self.right is None:
                self.right = self.__class__(val=val)
            else:
                self.right.addNode(val)
        else:
            if self.left is None:
                self.left = self.__class__(val=val)
            else:
                self.left.addNode(val=val)

    def printTreeLevel(self, level):
        print(level, " : ", self)
        if self.left:
            self.left.printTreeLevel(level+1)
        if self.right:
            self.right.printTreeLevel(level+1)

    def printTreeByLevel(self, root):
        """
        printing a tree level by level
        """

        if root is None:
            print("Root is None. Nothing to print!")

        frontier = [(0, root)]
        result = []

        while frontier != []:

            node_lvl, node = frontier.pop(0) # this is a queue
            result.append( (node_lvl, node.val) )

            for child in [node.left, node.right]:
                if child:
                    frontier.append( (node_lvl+1, child))


        for x in result:
            print("{} : {}".format(x[0], x[1]) )


if __name__ == "__main__":
    root = BSTNode(val=0)

    root.addNode(1)
    root.print()
