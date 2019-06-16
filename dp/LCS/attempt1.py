

class Solution:
    def LCS(self, str1, str2):
        """
        longest common subsequence
        """
        n1 = len(str1); n2 = len(str2)

        DP = [[""] * n2]* n1

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                print(i, j, str1[i:], str2[j:])

                # if j == n2-1:
                #     k = i
                #     while k < n1:
                #         if str1[k] == str2[j]:
                #             DP[i][j] = str1[k]
                #             break
                #         k += 1
                #     continue

                
                # if i == n1-1:
                #     k = j
                #     while k < n2:
                #         if str1[i] == str2[k]:
                #             DP[i][j] = str2[k]
                #             break
                #         k += 1
                #     continue

                # if n1 < n2 and i > j:
                #     DP[i][j] = DP[i][j+1]
                #     continue
                # if n1 > n2 and j < i: 
                #     DP[i][j] = DP[i+1][j]
                #     continue
                
                if str1[i] == str2[j]:
                    if i < n1-1 and j < n2-1:
                        DP[i][j] = str1[i] + DP[i+1][j+1]
                        continue
                    if i == n1-1 and j == n2-1:
                        DP[i][j] = str1[i]
                else:
                    if i < n1-1:
                        len1 = len(DP[i+1][j])
                    else:
                        len1 = 0
                    if j < n2-1:
                        len2 = len(DP[i][j+1])
                    else:
                        len2 = 0

                    if len1 == 0 and len2 == 0:
                        DP[i][j] = ""
                    else:
                        if len1 < len2:
                            DP[i][j] = DP[i][j+1]
                        else:
                            DP[i][j] = DP[i+1][j]

                #if j == 0 and i < n1-n2-1:
                #    DP[i][j] = DP[i][j+1]
                #    continue
                if i == 0 and j <= n2-n1:
                    DP[i][j] = DP[i+1][j]
                    continue

        return DP




def example_one():
    sol = Solution()

    str1 = "abc"
    str2 = "aabc"
    result = sol.LCS(str1, str2)

    for row in result:
        print(row)
    #print(result)

def example_two():
    sol = Solution()

    str1 = "abab"
    str2 = "cab"
    result = sol.LCS(str1, str2)

    for row in result:
        print(row)
if __name__ == '__main__':
    example_one()
    example_two()