from typing import List


"""
Example:
"aa"
"ab"
"abaa"

Note:
- require backtracking..

"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        check if s3 can be constructed by interleaving s1 and s2.
        """
        n1 = len(s1); n2 = len(s2); n3 = len(s3)

        if n1 + n2 != n3:
            return False

        if n1 == 0:
            return s2 == s3
        if n2 == 0:
            return s1 == s3
        
        i = 0
        j = 0
        k = 0
        while (i<n1 and j<n2 and k<n3):
            if s3[k] == s1[i]:
                i += 1
                k += 1
            elif s3[k] == s2[j]:
                j += 1
                k += 1
            else:
                return False
        return True





if __name__ == '__main__':

    inp = {'s1' : "aabcc", 
           's2' : "dbbca", 
           #'s3' : "aadbbcbcac"}
           's3' : "aadbbbaccc"}

    sol = Solution()
    result = sol.isInterleave(**inp)
    print(result)


    