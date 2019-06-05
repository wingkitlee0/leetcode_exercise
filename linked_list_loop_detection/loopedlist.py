"""
loop detection
"""

from linkedlist import LinkedList

class LoopDetection:
    """
    loop detection
    """
    @staticmethod
    def is_loop(head):
        """
        the classic slow/fast pointers implementation
        """

        if head.next is None:
            return False

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    @staticmethod
    def is_loop_hash(head):
        """
        implementation using hash-table
        """
        seen = {}
        curr = head
        while curr is not None:
            if curr not in seen:
                seen[curr] = 1
                curr = curr.next
            if curr in seen:
                return True
        return False


def main():
    """main"""
    head = LinkedList.create_random_int_list(10)
    LinkedList.print_linkedlist(head)

    # get tail
    print("catching the tail:")
    tail = head
    while tail.next is not None:
        tail = tail.next
    print("tail = ", tail.val, tail.next)

    # set the tail to 3
    print("set the tail to 3")
    curr = head
    while curr.next is not None:
        curr = curr.next
        if curr.val == 3:
            break
    print("curr = ", curr.val, curr.next)
    #tail.next = curr

    print(LoopDetection.is_loop(head))
    # LinkedList.print_linkedlist(head) # infinite

    print(LoopDetection.is_loop_hash(head))


if __name__ == '__main__':
    main()
