class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        if len(s) == 1:
            return s

        n = len(s)
        dp = [ [False]*n for _ in range(n)]
        
        result = (0, 0); maxlen = 0
        for i in range(n-1, -1, -1):
            for j in range(n):
                if i==j:
                    dp[i][i] = True # single character
                if j==i+1:
                    dp[i][j] = (s[i]==s[j])
                if j>=i+2:
                    if s[i]==s[j]:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    if j-i+1 > maxlen:
                        maxlen = j-i+1
                        result = (i, j)

        i_, j_ = result
        return s[i_:j_+1]

    def longestPalindrome_second_trial(self, s: str) -> str:

        n = len(s)

        dp = [ [False]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(n):
                if i==j:
                    dp[i][i] = True # single character
                if j==i+1:
                    dp[i][j] = (s[i]==s[j])
                if j>=i+2:
                    if s[i]==s[j]:
                        dp[i][j] = dp[i+1][j-1]

        found = False
        k = 0
        while k < n and not found:
            dj = 0
            while dj < k+1 and not found:
                i = dj; j = n-1-k+dj
                print(i, j, dp[i][j])
                found = dp[i][j]
                dj += 1
            k += 1
        i_ = i; j_ = j
        return s[i_:j_+1]

    def longestPalindrome_first_trial(self, s: str) -> str:

        n = len(s)

        dp = [ [False]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(n):
                if i==j:
                    dp[i][i] = True # single character
                if j==i+1:
                    dp[i][j] = (s[i]==s[j])
                if j>=i+2:
                    if s[i]==s[j]:
                        #print(i, j, s[i], s[j])
                        dp[i][j] = dp[i+1][j-1]

        found = False
        for k in range(n):
            for dj in range(k+1):
                i = dj; j = n-1-k+dj
                print(i, j, dp[i][j])
                if dp[i][j]:
                    i_ = i; j_ = n-1-i+dj
                    found = True
                    break
            if found:
                break


        found = False
        k = 0
        while k < n and not found:
            dj = 0
            while dj < k+1 and not found:
                i = dj; j = n-1-k+dj
                print(i, j, dp[i][j])
                found = dp[i][j]
                dj += 1
            k += 1
        i_ = i; j_ = j
#        i=0; j=0
#        while i < n and not found:
#            dj = 0
#            while dj < i+1 and not found:
#                j = n-1-i+dj
#                found = dp[i][j]
#                dj += 1
#            i += 1
#        i_ = i-1; j_ = j
        print(i_, j_)


        print("s = {}".format(s))
        for i in range(n):
            for j in range(n):
                print("({:1d},{:1d}):{:1}".format(i, j, dp[i][j]), end=' ')
                #print("{:1}".format(dp[i][j]), end=' ')
            print()

        return s[i_:j_+1]


if __name__ == '__main__':
    sol = Solution()

    input_list = [
        "babad",
        "cbbd",
        "abb",
        "ccc"
    ]

    for inp in input_list:
        result = sol.longestPalindrome(inp)
        print("{} : {}".format(inp, result))
        