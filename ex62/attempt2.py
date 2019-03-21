class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m:
            t = n; n = m; m = t

        if m==1 or n==1:
            return 1

        print("# (m, n) = ({},{}) ".format(m, n))
        for i in range(n):
            if i == 0:
                row = [1 for j in range(m)]
            else:
                print(row)
                for j in range(m-i):
                    if j==0:
                        row[j] = row[j+1] * 2
                    else:
                        row[j] = row[j-1] + row[j+1]
        return row[j]

if __name__ == "__main__":
    import sys 
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    sol = Solution()
    answer = sol.uniquePaths(m, n)
    print("# {}".format(answer))