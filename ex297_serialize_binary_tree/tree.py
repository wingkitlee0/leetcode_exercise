class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    @staticmethod
    def print_inorder(node):

        if node is not None:
            print(node.val)
            if node.left is not None:
                TreeNode.print_inorder(node.left)
            else:
                print("None")
            if node.right is not None:
                TreeNode.print_inorder(node.right)
            else:
                print("None")
            
