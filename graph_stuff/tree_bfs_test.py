from binarytree import Node
from collections import deque

class BinaryTree:
    @staticmethod
    def printNode(node):
        print(node)
        if node.left is not None:
            BinaryTree.printNode(node.left)
        if node.right is not None:
            BinaryTree.printNode(node.right)

    @staticmethod
    def put_in_queue(queue, node):
        queue.append(node)
        if node.left is not None:
            BinaryTree.put_in_queue(queue, node.left)
        if node.right is not None:
            BinaryTree.put_in_queue(queue, node.right)

    @staticmethod
    def print_bfs(node):
        """
        implementation using queue
        """
        queue = deque()
        curr = node
        while curr is not None:
            print(curr)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
            if len(queue) == 0:
                curr = None
            else:
                curr = queue.popleft()

    @staticmethod
    def print_bfs_recursive(queue, node):
        """
        implementation using recursion
        """
        if len(queue) == 0 and \
            not (node.left is None and node.right is None):
            # not last child
            print(node)
        if node.left is not None:
            queue.appendleft(node.left)
        if node.right is not None:
            queue.appendleft(node.right)

        while len(queue) > 0:
            curr = queue.pop()
            print(curr)
            BinaryTree.print_bfs_recursive(queue, curr)

    

def main():
    """
            1
           / \\
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    BinaryTree.printNode(root)

    queue = deque()
    BinaryTree.put_in_queue(queue, root)
    while len(queue) > 0:
        n = queue.popleft()
        print(n)

    print('---------------')
    BinaryTree.print_bfs_recursive(queue, root)

    print('---------------')
    BinaryTree.print_bfs(root)
    


    
if __name__ == '__main__':
    main()