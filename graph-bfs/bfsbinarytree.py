"""
BFS for binary tree
- modified from bfs.py
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binarytreeBFS(root):
    level = {root: 0}
    parent = {root: None}
    i = 1

    frontier = [root]
    while frontier:
        next = []
        for u in frontier:
            childs = []  # a list of childs if they are not None
            for x in [u.left, u.right]:
                childs += [x] if x is not None else []

            for x in childs:
                if x not in level:
                    level[x] = i
                    parent[x] = u
                    next.append(x)
        frontier = next
        i += 1

    return level, parent


if __name__ == "__main__":
    mytree = Node(5)
    mytree.left = Node(4)
    mytree.left.left = Node(3)
    mytree.left.right = Node(8)
    mytree.right = Node(6)
    mytree.right.left = Node(2)
    mytree.right.right = Node(10)

    level, parent = binarytreeBFS(mytree)

    level_r = dict()
    for k, v in level.items():
        if v not in level_r:
            level_r[v] = [k]
        else:
            level_r[v].append(k)

    for k, v in level_r.items():
        print(k, [x.val for x in v])

    print("----")
    for k, v in level.items():
        print(k.val, v)

    print("----")

    print(parent)
