class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1, n2 = len(word1), len(word2)

        if n1 == 0:
            return n2
        if n2 == 0:
            return n1

        

        if n1 < n2:
            word1, word2 = word2, word1 # swap the words s.t. word2 is shorter
            n1, n2 = n2, n1

        dp = [[None]*n2 for _ in range(n1)]
        
        seen_in_row = [False for _ in range(n1)]
        seen_in_col = [False for _ in range(n2)]
    
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):

                if i == n1-1 and j == n2-1:
                    minstep = 0
                    is_add, is_chg, is_rmv = False, False, False
                else:
                    # verbs w.r.t. word2
                    _add, _rmv, _chg = n1 * 2, n1 * 2, n1 * 2
                    
                    if j < n2-1:
                        _rmv = dp[i][j+1]
                    if i < n1-1:
                        _add = dp[i+1][j]
                    if i < n1-1 and j < n2-1:
                        _chg = dp[i+1][j+1]

                    minstep = min(_add, _rmv, _chg)
                    is_add = _add < _rmv and _add < _chg
                    is_chg = _chg < _add and _chg < _rmv
                    is_rmv = _rmv < _add and _rmv < _chg

                if word1[i] == word2[j]:
                    if is_add and seen_in_col[j]:
                        dp[i][j] = minstep + 1
                    else:
                        if is_rmv:
                            if not seen_in_row[i]:
                                dp[i][j] = minstep
                            else:
                                dp[i][j] = minstep + 1
                        else:
                            dp[i][j] = minstep    

                    seen_in_row[i] = True           
                    seen_in_col[j] = True           
                else:
                    dp[i][j] = minstep + 1

        #print(seen)

        return dp[0][0], dp


if __name__ == "__main__":
    
    input_list = [
        ("a", "ab"),
        ("abc", "ab"),
        ("abc", "abc"),
        ("abc", "abcd"),
        ("abc", "abcde"),
        ("aba", "ababa"),
        ("cedab", "ababac"),
        ("ab", "abxb"),
        ("ab", "abcb"),
        ("ab", "abcd"),
        ("teacher", "acheer"),
        ("sea", "eat"),
    ]

    sol = Solution()
    for inp in input_list:
        result, dp = sol.minDistance(*inp)
        print("({}, {}) -> {}".format(inp[0], inp[1], result))
        for row in dp:
            print(" ".join(["{:3}".format(r) for r in row]))