class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        if n == 1:
            return s
        dp = [ [None]*n for _ in range(n)]
        best = (0, 1)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if j == i+1:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1
                else: # j > i
                    if s[i] != s[j]:
                        if dp[i][j-1] > dp[i+1][j]:
                            dp[i][j] = dp[i][j-1]
                            best = (i, j-1)
                        else:
                            dp[i][j] = dp[i+1][j]
                            best = (i+1, j)
                    else:
                        dp[i][j] = dp[i][j-1] + 2

        return s[best[0]:best[1]]

    def longestPalindrome_verbose(self, s: str) -> str:

        n = len(s)

        dp = [ [None]*n for _ in range(n)]

        best = (0, 1)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
#                print( "({},{})".format(i, j) , end=" ")
                if j == i+1:
                    if s[i] == s[j]:
                        best = (i, i+2)
                        dp[i][j] = 2
                    else:
                        best = (i, i+1)
                        dp[i][j] = 1
                else: # j > i
                    if s[i] != s[j]:
                        if dp[i][j-1] > dp[i+1][j]:
                            dp[i][j] = dp[i][j-1]
                            best = (i, j-1)
                        else:
                            dp[i][j] = dp[i+1][j]
                            best = (i+1, j)
                    else:
                        best = (best[0], best[1]+1)
                        dp[i][j] = dp[i][j-1] + 2

        for i in range(n):
            for j in range(n):
                x = dp[i][j]
                if x:
                    print("{:2d}".format(x), end=" ")
                else:
                    print("  ", end=" ")
            print()

        print("best = ", best)

        return s[best[0]:best[1]]


if __name__ == '__main__':
    sol = Solution()

    input_list = [
        "babad",
        "cbbd",
        "bb",
        "ccc"
    ]

    for inp in input_list:
        result = sol.longestPalindrome_verbose(inp)
        print("{} : {}".format(inp, result))
        