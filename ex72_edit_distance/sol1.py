class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1, n2 = len(word1), len(word2)

        if n1 == 0:
            return n2
        if n2 == 0:
            return n1

        dp = [[None]*n2 for _ in range(n1)]

        if n1 < n2:
            word1, word2 = word2, word1 # swap the words s.t. word2 is shorter

        i, j = n1-1, n2-1

        while i >= 0 and j >= 0:
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
                # verbs w.r.t. word2
                _add, _rmv, _chg = float('inf'), float('inf'), float('inf')
                
                if j < n2-1:
                    _add = dp[i][j+1] + 1
                if i < n1-1:
                    _rmv = dp[i+1][j] + 1
                if i < n1-1 and j < n2-1:
                    _chg = dp[i+1][j+1] + 1

                dp[i][j] = min(_add, _rmv, _chg)

            if i == 0 and j == 0:
                break
            else:
                if i > 0:
                    i -= 1
                if j > 0:
                    j -= 1
                elif j == 0:
                    j = n2-1




        return dp[0][0]


if __name__ == "__main__":
    
    input_list = [
        ("abc", "ab"),
    ]

    sol = Solution()
    for inp in input_list:
        result = sol.minDistance(*inp)
        print("({}, {}) -> {}".format(inp[0], inp[1], result))