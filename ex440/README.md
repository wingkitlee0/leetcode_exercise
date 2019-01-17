440. K-th Smallest in Lexicographical Order
Hard

136

25

Favorite

Share
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

-----------------------

1. create a BST with maximum k members
2. if inserting k+1 member:
    if count > k:
        remove max
3. find k-th max:
    
    