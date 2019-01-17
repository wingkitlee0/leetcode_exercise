import numpy as np 
from tree import Tree
from lexicographical import compare

N = 20
k = 4

np.random.seed(1234)
lst = [1,2,3,4,11,12,13,14,21,22,23,24]

print(lst)

t = Tree(lst[0], compare=compare)

print("compare 2, 11 = ", t.compare(2,11) )
count = 1
for l in lst[1:]:
    t.addNode(l)
    count += 1
    if count > k:
        t = t.del_max()
        count -= 1

t.printTree()

print(t.find_max())



