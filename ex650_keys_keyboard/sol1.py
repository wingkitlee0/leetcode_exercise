class Solution:
    def minSteps(self, n: int) -> int:
        print("input: {}".format(n))
        if n == 0 or n == 1:
            return 0
            
        if n % 2 == 1:
            return n
        else:
            return 2 + self.minSteps(n//2)

if __name__ == '__main__':

    sol = Solution()
    for i in range(15):
        result = sol.minSteps(i)
        print("{}: {}".format(i, result))
        