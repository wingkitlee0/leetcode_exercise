import numpy as np 
from tree import Tree
from lexicographical import compare

np.random.seed(1234)
lst = np.random.randint(0,50,10)

print(lst)

t = Tree(lst[0])
for l in lst[1:]:
    t.addNode(l)

t.printTree()

t = t.del_max()

print("head = ", t.val)
if t.right is not None:
    print("head.right = ", t.right.val)

t.printTree()

for _ in range(5):
    print("remove..")
    t = t.del_max()
    t.printTree()