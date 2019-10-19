class Solution:
    def isMatch(self, s: str, p: str, verbose=False) -> bool:
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
    ]

    sol = Solution()
    for t in testcases:
        result = sol.isMatch(**t)
        print("{:<20} {:<20}: {}".format(t['s'], t['p'], result))
    