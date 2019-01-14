from tree import Tree

def printTree(t):
    if t is not None:
        if t.left is not None:
            printTree(t.left)
        print(" %s " % t.val)
        if t.right is not None:
            printTree(t.right)

def f(a, b, node):
    if node.left is not None or node.right is not None:
        if node.val < a and node.right is not None:
            return f(a, b, node.right)
        elif node.val >= b and node.left is not None:
            return f(a, b, node.left)
        else:
            L = f(a, node.val, node.left)
            R = f(node.val, b, node.right)
            return L + R + node.val
    else:
        if node.val >= a and node.val < b:
            return node.val       

if __name__ == "__main__":
    this = Tree(5)
    this.left = Tree(3)
    this.left.left = Tree(1)
    this.left.right = Tree(4)
    this.right = Tree(8)
    this.right.right = Tree(10)
    this.right.left = Tree(6)

    printTree(this)


    print(f(4, 7, this))