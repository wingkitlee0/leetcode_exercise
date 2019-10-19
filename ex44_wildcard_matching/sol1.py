class Solution:
    def isMatch(self, s: str, p: str, verbose=False) -> bool:
        ns = len(s)
        np = len(p)

        if s=='':
            return p == '*'
        if p=='*':
            return True
        
        def DP(i, j):
            if verbose:
                print(i, j, s[i], p[j])
            
            if p[j] == '*':
                if j == np-1:
                    # last char of p = '*'
                    # return True because of calling order
                    return True 
                else:
                    # not last char of p
                    # move to the end of '*'
                    k = j+1
                    while k <= np-2: # if p[k] is not last
                        if p[k] == '*':
                            k += 1
                        else:
                            break
                    if k == np-1:
                        if p[k] == '*':
                            return True
                        else:
                            l = i
                            while l <= ns-2:
                                if s[l] != p[k]:
                                    l += 1
                                else:
                                    break
                            if 
                            



            if i == ns-1 and p[j] == '*':
                if j <= np-2: # last char of s but not p
                    
                else: # last char of s w/ last char of p='*'
                    return True
            if p[j] == '?' or p[j] == s[i]:
                if i <= ns-2:
                    if j <= np-2:
                        return DP(i+1, j+1)
                    else:
                        return False
                else:
                    if j <= np-2: # last char of s but not p
                        k = j+1
                        while k <= np-2:
                            if p[k] == '*':
                                k += 1
                            else:
                                return False
                        return True
                    else: # last char of s and p
                        return s[i] == p[j]
            elif p[j] == '*':
                if j == np-1: # if '*' is last char
                    return True
                else:
                    k=i
                    while k <= ns-2 and s[k] != p[j+1]:
                        k += 1

                    if s[k] == p[j+1]:
                        if k < ns-1:
                            if j+1 < np-1:
                                return DP(k+1, j+2)
                            else:
                                return False
                        else:
                            return True
                    else:
                        return False

            else:
                return False
                        
        return DP(0, 0)
                        
                




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
    