
class BST:
    val = None
    left = None
    right = None

def convert(arr):
    # print(arr)
    if arr == []:
        return None

    if type(arr) == int:
        r = BST()
        r.val = arr
        return r

    n = len(arr) // 2
    r = BST()
    r.val = arr[n]
    if n >= 1:
        r.left = convert(arr[:n])
        r.right = convert(arr[n+1:])
    return r

def printBST(bst):
    if bst.left != None:
        printBST(bst.left)
    print("{} ".format(bst.val), end="")
    if bst.right != None:
        printBST(bst.right)
    


if __name__ == '__main__':
    b = convert([1,2,3,4,5,6,7])
    printBST(b)
    print("")

    b2 = convert([1,2,3,4,5,6])
    printBST(b2)
    print("")

    b3 = convert([1,2,3,4,5])
    printBST(b3)
    print("")



