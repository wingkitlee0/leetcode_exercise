"""
linked list
"""
import random


class Node:
    """
    node class
    """
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

    def is_none(self):
        """return True if .next is none"""
        return self.next is None


class LinkedList:
    """
    Linked List
    """
    @staticmethod
    def create_random_int_list(length=10):
        """
        create a singly linked list with random integers
        """
        nums = random.sample(range(0, length), length)
        print(nums)
        head = Node(nums[0])
        curr = head
        for num in nums[1:]:
            curr.next = Node(num)
            curr = curr.next
        return head

    @staticmethod
    def print_linkedlist(head):
        """
        print each element of linked list (without loop detection)
        """
        curr = head
        while curr is not None:
            print(curr.val, end=" ")
            if curr.next is None:
                # print('here')
                break
            else:
                curr = curr.next
        print("")


def main():
    """main"""
    head = LinkedList.create_random_int_list(10)
    LinkedList.print_linkedlist(head)


if __name__ == '__main__':
    main()
