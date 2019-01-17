import numpy as np 
from tree import Tree
from lexicographical import compare

class Solution:
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        if n>1 and k>1:
            t = Tree(1, compare=compare)
            count = 1
            for l in range(2,n):
                t.addNode(l)
                count += 1
                if count > k:
                    t = t.del_max()
                    count -= 1
            return t.find_max()



np.random.seed(1234)
lst = [1,2,3,4,11,12,13,14,21,22,23,24]

print(lst)

t = Tree(lst[0], compare=compare)

print("compare 2, 11 = ", t.compare(2,11) )


t.printTree()

print(t.find_max())

