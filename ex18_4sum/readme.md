# # 18 4-sum

This is a simple extension of two-sum: create a dictionary first and loop through the whole array. The time complexity is O(n^3) ...

A better way is to create a dictionary such that key-value pairs are `arr[i]+arr[j] : (i, j)`. Any additional pair `(i, j)` with the same sum (key) will be appended to the list (value). After that, we first have two for-loops (for picking first two number) and obtain a list of pairs `(k,l)`. From that list, we generate the quadruple `(i, j, k, l)`.

