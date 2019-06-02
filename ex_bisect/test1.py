import bisect
import numpy as np

"""
To test the operator overloading
"""

class Node:
    def __init__(self, x):
        self.val = x

    def __str__(self):
        return str(self.val)

    def __gt__(self, other): # overloading >
        return self.val > other.val

    def __lt__(self, other): # overloading <
        return self.val < other.val


def main():

    # generate a sorted array of random floats
    randlist = [np.random.rand() for _ in range(5)]
    a = [Node(x) for x in sorted(randlist)]

    print("sorted array:")
    for x in a:
        print("{:10.3f}".format(x.val), end=" ")
    print("")

    # find the number
    i = bisect.bisect(a, Node(0.5))
    print("index of 0.5 in node-list : {}".format(i))


if __name__ == '__main__':
    main()
