from list_node import ListNode
from attempt1 import Solution

def trial1():

    sol = Solution()

    list1 = ListNode.from_list([1, 13, 15, 16])
    list2 = ListNode.from_list([2, 4, 5, 7])
    print("list1=", list1.to_list())
    print("list2=", list2.to_list())

    a, b = (list1, list2) if list1 < list2 else (list2, list1)
    root = a

    while a and b:
        print(f"Comparing {a} and {b}")
        if a < b:
            print(f"{a} < {b}")
            anext = a.next
            if anext is not None:
                print("a.next is not None")
                if anext < b:
                    # print(f"a.next < {b}")
                    a = a.next
                    continue
                else:
                    print(f"Inserting {b}. Advance a")
                    a.next, b.next, b = b, anext, b.next
                    a = a.next
            else:
                a.next, b = b, b.next
                break
        else:
            a = a.next

    print("result: ", root.to_list())


if __name__ == "__main__":
    trial1()
