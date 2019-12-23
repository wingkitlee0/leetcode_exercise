class Solution:
    
    def minDistance(self, word1: str, word2: str) -> int:
        """
        implementation using prefix instead of suffix
        """

        l1, l2 = len(word1), len(word2)
        
        # dp[i][j]: the edit distance of word1[:i] and word2[:j]
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        
        # initialize the left and top boundaries
        for i in range(l1+1):
            dp[i][0] = i        # index zero means empty str
        for i in range(l2+1):
            dp[0][i] = i
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                up = dp[i-1][j] + 1
                left = dp[i][j-1] + 1
                if word1[i-1] == word2[j-1]:
                    left_up = dp[i-1][j-1]
                else:
                    left_up = dp[i-1][j-1] + 1
                
                dp[i][j] = min(up, left, left_up)

        return dp[l1][l2], dp

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