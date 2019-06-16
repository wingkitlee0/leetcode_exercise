

class Solution:
    def LCS(self, str1, str2):
        """
        longest common subsequence
        """
        n1 = len(str1); n2 = len(str2)

        # swap the strings if str1 is longer
        if n1 > n2:
            str1, str2 = str2, str1
            n1, n2 = n2, n1

        # construct a DP matrix
        DP = [ [''] * n2 for _ in range(n1)]

        for i in range(n1-1, -1, -1):
            #print(DP)
            for j in range(n2-1, -1, -1):
                #print("{} {} : ".format(i,j), end="")
                
                # boundary
                if i == n1-1: # last row
                    # only one character is possible
                    if str1[i] == str2[j]:
                        DP[i][j] = str2[j]
                    else:
                        DP[i][j] = DP[i][j+1] if j+1<n2 else ""
                    #print("DP[{:1d}][{:1d}] = {}".format(i,j,DP[i][j]))
                    continue

                if j == n2-1: # last column
                    if i < n1-1:
                        # only one character is possible
                        DP[i][j] = str2[j] if str1[i] == str2[j] else ""
                        #print("DP[{:1d}][{:1d}] = {}".format(i,j,DP[i][j]))
                        continue
                
                if str1[i] == str2[j]:
                    #print("str1[i] == str2[j]: i={:1d}, j={:1d}".format(i,j))
                    if i < n1-1 and j < n2-1:
                        DP[i][j] = str1[i] + DP[i+1][j+1]
                        #print("DP[{:1d}][{:1d}] = {}".format(i,j,DP[i][j]))
                        continue
    
                else:
                    if i < n1-1:
                        len1 = len(DP[i+1][j])
                    else:
                        len1 = 0
                    if j < n2-1:
                        len2 = len(DP[i][j+1])
                    else:
                        len2 = 0

                    if len1 <= len2:
                            DP[i][j] = DP[i][j+1]
                    else:
                        DP[i][j] = DP[i+1][j]                        

        return DP[0][0]

def example_three(str1, str2):
    print("---------------")
    sol = Solution()
    result = sol.LCS(str1, str2)
    print("{} {} -> {} ".format(str1, str2, result))
    
if __name__ == '__main__':
    example_three("abc", "aabc")
    example_three("abab", "cab")
    example_three("aaa", "aaaaa")
    example_three("cabac", "abaccccc")