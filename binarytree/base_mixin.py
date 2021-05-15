from collections import deque

class BaseMixin:
    def print(self):
        """Print each node using __str__()"""
        if self.left:
            self.left.print()
        print(self)
        if self.right:
            self.right.print()

    def printTree(self, print_children: bool = False):
        if self.left:
            self.left.printTree(print_children=print_children)
        if print_children:
            left_val = self.left.val if self.left else None
            right_val = self.right.val if self.right else None
            print(f"{self.val}: ({left_val}, {right_val})")
        else:
            print(self.val)
        if self.right:
            self.right.printTree(print_children=print_children)

    def printTree_bfs(self):

        level = 0
        queue = [(level, self)]

        while queue != []:
            level, curr = queue.pop(0)
            if curr is not None:
                print("{} : {}".format(level, curr.val))
                for child in [curr.left, curr.right]:
                    queue.append((level + 1, child))
            else:
                print("{} : {}".format(level, None))

    def printTree_bfs2(self):

        level = 0
        queue = deque()
        queue.append((level, self))

        while queue:
            level, curr = queue.popleft()
            if curr is not None:
                print("{} : {}".format(level, curr.val))
                for child in [curr.left, curr.right]:
                    queue.append((level + 1, child))
            else:
                print("{} : {}".format(level, None))