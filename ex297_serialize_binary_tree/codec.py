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
                output += "None,"
            else:
                queue.appendleft(curr.left)
            
            if curr.right is None:
                output += "None,"
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

        queue = deque()
        for x in data[1:-2].split(','):
            queue.appendleft(x)

        print(len(queue))
        while len(queue) > 0:
            x = queue.pop()
            print(x)

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

def example_one():
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

if __name__ == '__main__':
    example_one()

    