from typing import List
from binarytree import TreeNode

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return []

def get_two_trees_inorder(left, right):

    if left is None and right is None:
        return []

    first = True
    result = []
    lstack, rstack = [], []
    lvalue, rvalue = None, None
    visited = set()

    while first or lstack or rstack:
        print("left-stack:  ", [s.val for s in lstack])
        print("right-stack: ", [s.val for s in rstack])
        print("visited:     ", [v.val for v in visited])
        

        if first:
            lcurr, rcurr = left, right # either of them could be None
            first = False
        else:
            if lvalue is None:
                if lstack:
                    lcurr = lstack.pop()
                else:
                    lcurr = None
            if rvalue is None:
                if rstack:
                    rcurr = rstack.pop()
                else:
                    rcurr = None

        if lcurr is not None:
            print("lcurr: ", lcurr.val)
            if lcurr in visited or (lcurr.left is None and lcurr.right is None):
                lvalue = lcurr.val
                visited.add(lcurr)
            else:
                lvalue = None
        
        if rcurr is not None:
            print("rcurr: ", rcurr.val)
            if rcurr in visited or (rcurr.left is None and rcurr.right is None):
                rvalue = rcurr.val
                visited.add(rcurr)
            else:
                rvalue = None

        print(lvalue, rvalue)


        if lvalue is not None and rvalue is not None:
            if lvalue < rvalue:
                result.append(lvalue)
                lvalue = None
            else:
                result.append(rvalue)
                rvalue = None
        
        if len(lstack) == 0 and rvalue is not None:
            result.append(rvalue)
            rvalue = None
        if len(rstack) == 0 and lvalue is not None:
            result.append(lvalue)
            lvalue = None

        print("result: ", result)
        print(lvalue, rvalue)

        if lvalue is None and lcurr not in visited and lcurr is not None:
            if lcurr.right:
                lstack.append(lcurr.right)
            lstack.append(lcurr)
            if lcurr.left:
                lstack.append(lcurr.left)
            visited.add(lcurr)
        
        if rvalue is None and rcurr not in visited and rcurr is not None:
            if rcurr.right:
                rstack.append(rcurr.right)
            rstack.append(rcurr)
            if rcurr.left:
                rstack.append(rcurr.left)
            visited.add(rcurr)

        print("*left-stack: {} ".format([s.val for s in lstack]))
        print("*right-stack:  ", [s.val for s in rstack])
        
    return result






def main():

    list1 = [5,2,8,1,3,7,9]
    list2 = [4,0,6]

    tree1 = TreeNode.list2tree(list1)
    tree2 = TreeNode.list2tree(list2)

    result = get_two_trees_inorder(tree1, tree2)
    print(result)




if __name__ == "__main__":
    main()
