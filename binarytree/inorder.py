from binarytree import TreeNode

def get_inorder_iterative(tree):

    if tree is None:
        return []

    first = True
    result = []
    stack = []
    visited = set()

    while stack or first:
        if first:
            curr = tree
            first = False
        else:
            curr = stack.pop()

        print("stack:  ", [s.val for s in stack])
        print("result: ", result)
        print("curr:   ", curr.val)

        if curr in visited:
            result.append(curr.val)
            continue
        
        if curr.left is None and curr.right is None: # append to the list if that's a leave
            result.append(curr.val)
            continue

        if curr.right:
            stack.append(curr.right)
        stack.append(curr)
        if curr.left:
            stack.append(curr.left)

        visited.add(curr)

        
    return result


def main():
    input_list = [
        [5, 2, 8, 1, 3, 7, 9],
        [2, 1, 3],
    ]

    for lst in input_list:
        tree = TreeNode.list2tree(lst)

        result = get_inorder_iterative(tree)
        print(f"{lst} -> {result}")


if __name__ == "__main__":
    main()