# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from binarytree import TreeNode

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return []

def tree2list(tree):

    if tree is None:
        return []

    queue = [tree]

    result = []

    seen = set()
    first = True
    while queue:
        print(queue)
        curr = queue.pop(0)
        if len(seen) > 0 and curr in seen: continue
        if not first:
            result.append(curr.val)
        else:
            first = False
        seen.add(curr)
        
        if curr.left is not None:
            queue.append(curr.left)
        queue.append(curr)
        if curr.right is not None:
            queue.append(curr.right)

    return result

def dfs(tree):

    if tree is None:
        return

    if tree.left is not None:
        dfs(tree.left)
    print(tree.val)
    if tree.right is not None:
        dfs(tree.right)

def dfs2(tree1, tree2):

    if tree1 is None:
        if tree2 is None:
            return
        else:
            dfs(tree2)
    else:
        if tree2 is None:
            dfs(tree1) 

    if tree1.left is not None:
        if 
        dfs(tree.left)
    print(tree.val)
    if tree1.right is not None:
        dfs(tree.right)

# def twotree2list(tree1, tree2):

#     if tree1 is None:
#         if tree2 is None:
#             return []
#         else:
#             return tree2
#     else:
#         if tree2 is None:
#             return tree1

#     queue = [tree1, tree2] if tree1.val 

#     result = []

#     seen = set()
#     while queue:
#         print(queue)
#         curr = queue.pop()
#         if curr in seen: continue
#         result.append(curr.val)
#         seen.add(curr)
        
#         if curr.left is not None:
#             queue.append(curr.left)
#         queue.append(curr)
#         if curr.right is not None:
#             queue.append(curr.right)

    # return result

def main():

    root1 = [5,2,8,1,3,7,9]

    tree = TreeNode.list2tree(root1)

    # result = tree2list(tree)
    # print(result)

    dfs(tree)

if __name__ == "__main__":
    main()
