# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque
from tree import TreeNode

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        queue = deque()

        output = "["

        curr = root
        while curr is not None:
            output += "{},".format(curr.val)
            print(curr.val)

            if curr.left is None:
                if curr.val is not None:
                    # put a node for None such that it would print it out at the next level
                    queue.appendleft(TreeNode(None))
            else:
                queue.appendleft(curr.left)

            if curr.right is None:
                if curr.val is not None:
                    queue.appendleft(TreeNode(None))
            else:
                queue.appendleft(curr.right)

            if len(queue) > 0:
                curr = queue.pop()
            else:
                curr = None

        output += "]"

        return output

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None

        queue = deque()
        for x in data[1:-2].split(','):
            queue.appendleft(x)

        print(len(queue))
        level = 0
        
        parent_list = []
        if len(queue) > 0:
            val = queue.pop()
            root = TreeNode(val)
            parent_list.append(root)
    
        while len(parent_list) > 0:
            children_list = []
            for parent in parent_list:
                L = queue.pop()
                R = queue.pop()

                if L != "None":
                    parent.left = TreeNode(L)
                    children_list.append(parent.left)
                
                if R != "None":
                    parent.right = TreeNode(R)
                    children_list.append(parent.right)


            parent_list = children_list

        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

def example_one():
    print("example one")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    output_string = codec.serialize(root)
    print(output_string)

    for x in output_string[1:-1].split(','):
        print(x)

    print("calling deserialize")
    codec.deserialize(output_string)


def example_two():
    print("example two")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)


    print("--------------inorder-------")
    TreeNode.print_inorder(root)

    codec = Codec()
    output_string = codec.serialize(root)
    print(output_string)

    for x in output_string[1:-1].split(','):
        print(x)

    print("calling deserialize")
    new_root = codec.deserialize(output_string)

    TreeNode.print_inorder(new_root)

def example_three():

    string = "[1,2,3,None,4,None,5,None,None,None,None,]"

    codec = Codec()

    new_string = codec.serialize(codec.deserialize(string))
    print(string)
    print(new_string)


if __name__ == '__main__':
    example_one()
    example_two()
    example_three()
