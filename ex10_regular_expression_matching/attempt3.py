"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""

class Solution:
    def isMatch(self, s=None, p=None, **kwargs):

        ns = len(s)
        np = len(p)

        if np == 0:
            return False
        if np == 1:
            if p[0] == s[0] or p[0] == '.':
                return ns == 1
            elif p[0] == '*':
                return True
            else:
                return False

        dp = [[False]*ns for _ in range(np)] # dp[j][i]

        for j in range(np-1, -1, -1):
            for i in range( (ns-np)+j,-1, -1):
                print("({}, {}) compare {} and {}".format(i, j, s[i:], p[j:]))

                if p[j] == s[i] or p[j] == '.':
                    if j == np-1 and i == ns-1:
                        dp[j][i] = True
                    if j <= np-2 and i <= ns-2:
                        dp[j][i] = dp[j+1][i+1]

            if p[j] == '*':
                for i in range((ns-np)+j, -1, -1):
                    dp[j][i] = True
                    
        

        print("here")
        # for j in range(np):
        #     for i in range(ns):
        #         print(i, j, dp[j][i])
        for row in dp:
            print(row)
        return dp[0][0]

def main():

    inputlist = [
        { 's': "aa", 'p': "a"},
        { 's': "aaaa", 'p': 'a*a'},
        { 's': "aa", 'p': "a."},
        { 's': "aaa", 'p': "a.a"},
        { 's': "ab", 'p': ".*"},
        { 's': "aab", 'p': "c*a*b"},
        { 's': "mississippi", 'p': "mis*is*p*"}
    ]

    answerlist = [
        False,
        True,
        True,
        True,
        True,
        False,
        False
    ]

    sol = Solution()
    for inp, ans in zip(inputlist, answerlist):
        result = sol.isMatch(**inp)

        print("s={:12s} p={:12s} : {!s:>5} (answer: {!s:>5})".format(
            inp['s'], inp['p'], result, ans))

    print("{!s:>5} {}".format(True, False))

if __name__ == "__main__":
    main()