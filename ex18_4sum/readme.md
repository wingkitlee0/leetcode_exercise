# # 18 4-sum

This is a simple extension of two-sum: create a dictionary first and loop through the whole array. The time complexity is O(n^3) ...

A better way is to create a dictionary such that key-value pairs are `arr[i]+arr[j] : (i, j)`.

