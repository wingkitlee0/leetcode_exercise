"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""

class Solution:
    def isMatch(self, s=None, p=None, **kwargs):

        return False

def main():

    inputlist = [
        { 's': "aa", 'p': "a"},
        { 's': "aa", 'p': "a*"},
        { 's': "aaa", 'p': "a*"},
        { 's': "ab", 'p': ".*"},
        { 's': "aab", 'p': "c*a*b"},
        { 's': "mississippi", 'p': "mis*is*p*"}
    ]

    answerlist = [
        False,
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