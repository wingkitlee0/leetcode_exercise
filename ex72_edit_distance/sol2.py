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

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):

                if word1[i] == word2[j]:
                    if i == n1-1: # last row of dp
                        if j == n2-1:
                            dp[i][j] = 0
                        else:
                            dp[i][j] = dp[i][j+1]
                    else: # i < n1-1
                        if j == n2-1:
                            dp[i][j] = dp[i+1][j]
                        else:
                            dp[i][j] = dp[i+1][j+1] 

                else:
                    if i == n1-1 and j == n2-1:
                        dp[i][j] = 1
                    else:
                        # verbs w.r.t. word2
                        _add, _rmv, _chg = n1 * 10, n1 * 10, n1 * 10
                        
                        if j < n2-1:
                            _add = dp[i][j+1] + 1
                        if i < n1-1:
                            _rmv = dp[i+1][j] + 1
                        if i < n1-1 and j < n2-1:
                            _chg = dp[i+1][j+1] + 1

                        dp[i][j] = min(_add, _rmv, _chg)




        return dp[0][0], dp


if __name__ == "__main__":
    
    input_list = [
        ("abc", "ab"),
        ("abc", "abc"),
        ("abc", "abcd"),
        ("abc", "abcde"),
        ("aba", "ababa")
    ]

    sol = Solution()
    for inp in input_list:
        result, dp = sol.minDistance(*inp)
        print("({}, {}) -> {}".format(inp[0], inp[1], result))
        for row in dp:
            print(" ".join([str(r) for r in row]))