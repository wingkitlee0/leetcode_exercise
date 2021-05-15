import logging
from collections import deque
from dataclasses import dataclass
from typing import Any

from binarytree import BaseMixin, BaseNode

logger = logging.getLogger(__name__)


@dataclass
class BSTNode(BaseMixin, BaseNode):
    def __post_init__(self):
        logger.debug("Created a node with val=%s", self.val)

    def addNode(self, val: Any) -> None:
        if val >= self.val:
            if self.right is None:
                logger.debug("  Adding node %s with parent %s", val, self.val)
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
            self.left.printTreeLevel(level + 1)
        if self.right:
            self.right.printTreeLevel(level + 1)

    def print_tree_by_level(self):
        """Printing a tree level by level"""

        frontier = deque([(0, self)])
        result = []

        while frontier:

            node_lvl, node = frontier.popleft()  # this is a queue
            result.append((node_lvl, node.val))

            for child in [node.left, node.right]:
                if child:
                    frontier.append((node_lvl + 1, child))

        for x in result:
            print("{} : {}".format(x[0], x[1]))
