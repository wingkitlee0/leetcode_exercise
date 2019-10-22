class Solution:
    def isMatch(self, s: str, p: str, verbose=False, memo=dict()) -> bool:
        """
        recursive solution
        """
        ns = len(s)
        np = len(p)

        if verbose:
            print(s, p)

        if (s, p) in memo:
            return memo[(s, p)]

        if np == 0:
            return ns == 0 # p == '' and s == ''
        else:
            # p is not empty
            if ns == 0:
                # if s is empty
                if p[-1] == '*':
                    memo[(s, p)] = self.isMatch(s[:], p[:-1], verbose=verbose, memo=memo)
                    return memo[(s, p)]
                else:
                    memo[(s, p)] = False
                    return memo[(s, p)]
            else:
                # if s is not empty
                if p[-1] == s[-1] or p[-1] == '?':
                    memo[(s, p)] = self.isMatch(s=s[:-1], p=p[:-1], verbose=verbose, memo=memo)
                    return memo[(s, p)]
                elif p[-1] == '*':
                    memo[(s, p)] = self.isMatch(s[:], p[:-1], verbose=verbose, memo=memo) \
                                    or self.isMatch(s[:-1], p[:], verbose=verbose, memo=memo)
                    return memo[(s, p)]
                else:
                    memo[(s, p)] = False
                    return memo[(s, p)]

    def isMatch_1(self, s: str, p: str, verbose=False) -> bool:
        """
        recursive solution: working without memo
        """
        ns = len(s)
        np = len(p)

        if verbose:
            print(s, p)

        if np == 0:
            return ns == 0 # p == '' and s == ''
        else:
            # p is not empty
            if ns == 0:
                # if s is empty
                if p[-1] == '*':
                    return self.isMatch(s[:], p[:-1], verbose=verbose)
                else:
                    return False
            else:
                # if s is not empty
                if p[-1] == s[-1] or p[-1] == '?':
                    return self.isMatch(s=s[:-1], p=p[:-1], verbose=verbose)
                elif p[-1] == '*':
                    return self.isMatch(s[:-1], p[:], verbose=verbose) \
                        or self.isMatch(s[:], p[:-1], verbose=verbose)
                else:
                    return False




    def isMatch_old(self, s: str, p: str, verbose=False) -> bool:
        ns = len(s)
        np = len(p)

        if verbose:
            print(s, p)

        if s == p:
            return True

        if p in ['', '*']:
            return True
        
        if p == '?':
            return ns == 1

        if p[0] == '*':
            print("first char of p is *")
            j = 0
            while j <= np-2:
                if p[j] == '*':
                    j += 1
                else:
                    break

            if j == np-1:
                return self.isMatch(s[1:], p[j:], verbose=verbose)
            else:
                print("p[j] != '*': ", p[j])
            
                if ns == 0:
                    return False
                elif ns == 1:
                    return s[0] == p[j]
                else:
                    if s[0] == p[j]:
                        return self.isMatch(s[1:], p[j+1:], verbose=verbose)
                    else:
                        return False
        else:
            if ns == 0:
                return False
            else:
                if p[0] == '?' or p[0] == s[0]:
                    print("{}={}. Now check ".format(s[0], p[0]), s[1:], p[1:])
                    return self.isMatch(s[1:], p[1:], verbose=verbose)                    
                else:
                    return False

                        
                




if __name__ == '__main__':
    testcases = [
        {'s': 'aa', 'p': 'a'},
        {'s': 'aa', 'p': '*'},
        {'s': 'cb', 'p': '?a'},
        {'s': 'adceb', 'p': '*a*b'},
        {'s': 'acdcb', 'p': 'a*c?b'},
        {'s': 'aa', 'p': 'a*'},
        {'s': 'aa', 'p': 'aa*'},
        {'s': 'aa', 'p': 'a**'},
        {'s': 'aa', 'p': 'a**a', 'verbose':True},
        {'s': 'aa', 'p': 'a*c', 'verbose':True},
        {'s': 'aabab', 'p': 'a*b', 'verbose':False},
        {'s': 'ab', 'p': '**ab', 'verbose':False},
        {'s': "abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab", 'p': "*aabb***aa**a******aa*"}
    ]

    sol = Solution()
    for t in testcases:
        result = sol.isMatch(**t)
        print("{:<20} {:<20}: {}".format(t['s'], t['p'], result))
    