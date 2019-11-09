from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        n = len(s)

        frontier = [(0, j+1, 0) for j in range(3)]
        k = 0

        while frontier != [] and k <= 5:
            i, j, k = frontier.pop() # i, j for s[i:j] and k as level
            curr = s[i:j]
            
            if len(curr) == 0 or int(curr) >= 256:
                continue
            else:
                for dj in range(3):
                    if j+dj+1 < n:
                        frontier.append( (j, j+dj+1, k+1))

            print(k, curr)
            
#            print(curr)


        #print(frontier)
        return 0


if __name__ == '__main__':
    sol = Solution()

    input_list = ["25525511135"]

    for inp in input_list:
        result = sol.restoreIpAddresses(inp)

        print(result)