"""
Note:
- 1 <= A.length == B.length <= 20
- A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}
"""
from collections import defaultdict

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        def swap_char(A: str, i: int, j: int) -> str:
            temp = [x for x in A]
            temp[i], temp[j] = temp[j], temp[i]
            return "".join(temp)            

        swap = lambda s, i, j: s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

        if A == "" or B == "":
            return 0

        if A == B:
            return 0

        while A[-1] == B[-1]:
            A = A[:-1]
            B = B[:-1]

        loc_A = defaultdict(list, []) # key, value = character, list of locations
        for i, x in enumerate(A):
            loc_A[x].append(i)

        # first step, pick the last character of B
        n = len(B)
        # use the queue to store: K-step, source ch idx, target character idx
        queue = [(1, i, n-1, A) for i in loc_A[B[n-1]]]
        visited = set([A])

        j = n-1
        while queue and j>0:
            print(queue)
            k, i, j, s = queue.pop(0)
            #curr = swap_char(s, j, i)
            curr = swap(s, i, j)
            print("({:1d},{:1d},{:1d}): {}".format(k,i,j,curr))
            if curr[:j] == B[:j]:
                break

            loc_ = defaultdict(list, [])
            for idx, x in enumerate(curr[:j]):
                loc_[x].append(idx)
            
            while j>0 and curr[j] == B[j]:
                j -= 1
            
            print(loc_)
            if curr not in visited:
                visited.add(curr)
                queue.extend( [(k+1, i, j, curr) for i in loc_[B[j]]] )

        return k

if __name__ == '__main__':

    sol = Solution()

    input_list = [
        {'A': 'ab', 'B': 'ba'},
        {'A': "abc", 'B': "bca"},
        {'A': "abac", 'B': "baca"},
        {'A': "aabc", 'B': "abca"},
    ]

    for inp in input_list:
        print("input: ", inp)
        result = sol.kSimilarity(**inp)
        print("output:", result)
        print()
