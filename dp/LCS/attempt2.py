

class Solution:
    def LCS(self, str1, str2):
        """
        longest common subsequence
        """
        n1 = len(str1); n2 = len(str2)

        if n1 > n2:
            str1, str2 = str2, str1
            n1, n2 = n2, n1

        DP = [[""] * n2]* n1

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):

                if j == 0:
                    print("here", n1, n2, n2-n1)
                    if n2 > n1 and i < n2-n1:
                        
                        curr = DP[i][j+1]
                        
                        print("here", i, j, curr)
                        DP[i][j] = curr
                        continue
                

                
                
                if str1[i] == str2[j]:
                    if i < n1-1 and j < n2-1:
                        curr = str1[i] + DP[i+1][j+1]
                        
                    if j == n2-1:
                        curr = str2[j]
                    if i == n1-1:
                        curr = str1[i]
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
                        curr = ""
                    else:
                        if len1 < len2:
                            curr = DP[i][j+1]
                        else:
                            curr = DP[i+1][j]

                print("{} {} {:>10} {:>10} {}".format(i, j, str1[i:], str2[j:], len(curr) ))
                DP[i][j] = curr

        return DP[0][0]




def example_one():
    sol = Solution()

    str1 = "abc"
    str2 = "aabc"
    result = sol.LCS(str1, str2)

    #for row in result:
    #    print(row)
    print(result)

def example_two():
    sol = Solution()

    str1 = "abab"
    str2 = "cab"
    result = sol.LCS(str1, str2)
    print(result)
    #for row in result:
    
    #    print(row)

def example_three():
    sol = Solution()

    str1 = "aaaba"
    str2 = "bcaaa"
    result = sol.LCS(str1, str2)
    print(result)
    #for row in result:
    #    print(row)
if __name__ == '__main__':
    example_one()
    example_two()
    example_three()