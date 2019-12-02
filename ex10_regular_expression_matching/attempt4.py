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

        istart = 0
        prev = ''
        flag_single_ok = False
        for j in range(np):
            print("(j, istart, prev) = ({}, {}, {})".format(j, istart, prev))
            if p[j] == '*':
                print("p[j] = * at j = {} and prev = {}".format(j, prev))
                if j > 0:
                    if p[j-1] != '*' and flag_single_ok:
                        istart -= 1
                    i = istart
                    print("({}, {}) compare {} and {}".format(i, j, s[:i+1], p[:j+1]))
                    if prev == '.':
                        while i < ns:
                            dp[j][i] = True
                            i += 1
                    else:
                        while i < ns and s[i] == prev:
                            dp[j][i] = True
                            i += 1
                    continue
                else:
                    print("error")
            else:
                flag_single_ok = False
                if j > 0 and p[j-1] == '*':
                    istart += 1

                for i in range(istart, ns):
                    print("({}, {}) compare {} and {}".format(i, j, s[:i+1], p[:j+1]), end=' ')

                    if p[j] == s[i] or p[j] == '.':
                        if j == 0 and i == 0:
                            dp[j][i] = True
                            istart = i + 1
                            prev = p[j]
                            flag_single_ok = True
                            print(True)
                            break
                        if j > 0 and i > 0 :
                            dp[j][i] = dp[j-1][i-1]
                            istart = i + 1
                            prev = p[j]
                            flag_single_ok = True
                            print(True)
                            break
                    print(False)

            if j == np-1:
                for i in range(istart, ns):
                    dp[j][i] = dp[j-1][i-1]

        # print("here")
        for row in dp:
            print(row)
        return dp[-1][-1]

def main():

    inputlist = [
        { 's': "aa", 'p': "a"},
        { 's': "aaaa", 'p': 'a*a'},
        { 's': "aa", 'p': "a."},
        { 's': "aaa", 'p': "a.a"},
        { 's': "ab", 'p': ".*"},
        { 's': "aab", 'p': "c*a*b"},
        { 's': "mississippi", 'p': "mis*is*p*"},
        { 's': "ssissi", 'p': "s*is*i"},
        { 's': "mississippi", 'p': "mis*is*ip*."}
        
    ]

    answerlist = [
        False,
        True,
        True,
        True,
        True,
        True,
        False,
        True,
        True,
    ]

    sol = Solution()
    for inp, ans in zip(inputlist, answerlist):
        result = sol.isMatch(**inp)

        print("s={:12s} p={:12s} : {!s:>5} (answer: {!s:>5})".format(
            inp['s'], inp['p'], result, ans))

if __name__ == "__main__":
    main()