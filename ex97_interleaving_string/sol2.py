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

        memo = {}
        def dfs(i, j):
            k = i+j # this is a must!
            #print("Comparing ({}, {}) to {}".format(s1[i:], s2[j:], s3[k:]))

            if (i, j) in memo:
                return memo[(i, j)]

            if i == n1:
                if j == n2:
                    memo[(i, j)] = True
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = s2[j] == s3[k] and dfs(i, j+1)
                    return memo[(i, j)]
            else:
                if j == n2:
                    memo[(i, j)] = s1[i] == s3[k] and dfs(i+1, j)
                    return memo[(i, j)]
            

            if s1[i] == s3[k]:
                if s2[j] == s3[k]:
                    memo[(i, j)] = dfs(i+1, j) or dfs(i, j+1)
                    return memo[(i, j)]
                else:
                    # s1[i] == s3[k] only
                    memo[(i, j)] = dfs(i+1, j)
                    return memo[(i, j)]
            else:
                if s2[j] == s3[k]:
                    # s2[j] == s3[k] only
                    memo[(i, j)] = dfs(i, j+1)
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = False
                    return memo[(i, j)]

        return dfs(0, 0)

def main():
    input_list = [
        ['aabcc', 'dbbca', "aadbbcbcac"], # true
        ['aa', 'ab', 'abaa'], # true
        ["bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
        "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
        "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"], #
    ]

    sol = Solution()
    for inp in input_list:
        result = sol.isInterleave(*inp)

        print(inp, result)



if __name__ == '__main__':
    main()
    
    