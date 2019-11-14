import math

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        if n < 10:
            return k
        else:
            stack = [x for x in range(9, 0, -1)]

        j = 0 # number
        while stack and k:
            curr = stack.pop()
            print(j, curr)
            j += 1
            if j == k:
                break

            for i in range(9,-1, -1):
                x = curr*10 + i
                if x <= n:
                    stack.append(x)

        return curr

if __name__ == '__main__':

    sol = Solution()
    r = sol.findKthNumber(1, 1)
    print(r)
    r = sol.findKthNumber(10, 3)
    print(r)
    r = sol.findKthNumber(13, 5)
    print(r)
    print("-----")
    r = sol.findKthNumber(110, 5)
    print(r)