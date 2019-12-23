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

        # some large number as default values
        dp = [[n1*n2]*(n2+1) for _ in range(n1+1)] 

        # initialize the last row and last column
        for i in range(n1+1):
            dp[i][-1] = n1-i
        for j in range(n2+1):
            dp[-1][j] = n2-j

        # fill in the dp array
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                
                # verbs w.r.t. word2
                # no edge case needed
                _rmv = dp[i][j+1] + 1
                _add = dp[i+1][j] + 1

                if word1[i] == word2[j]:
                    _chg = dp[i+1][j+1]
                else:
                    _chg = dp[i+1][j+1] + 1

                dp[i][j] = min(_add, _rmv, _chg)
                    
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