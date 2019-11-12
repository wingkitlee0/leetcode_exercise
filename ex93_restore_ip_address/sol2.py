from typing import List
from collections import defaultdict

def valid_digits(s):
    ns = len(s)
    
    if ns >= 1:
        d = int(s)
        if ns == 1:
            return (0 <= d and d <= 9)
        elif ns == 2:
            return (10 <= d and d <= 99)
        elif ns == 3:
            return (100 <= d and d <= 255)
    else:
        return False


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        n = len(s)
        if n < 4 or n > 12:
            return []

        k = 0
        frontier = [(0, j, k) for j in range(1, 4) if valid_digits(s[:j])]

        result = defaultdict(list, [])
        valid_ends = []
        while frontier != [] and k <= 4:
            #print(k, frontier)
            i, j, k = frontier.pop() # i, j for s[i:j] and k as level
            curr = s[i:j]
            print(k, curr)

            for dj in range(1, 4):
                next = s[j:j+dj]
                if valid_digits(next) and j+dj <= n:
                    if k < 3:
                        frontier.append( (j, j+dj, k+1))

                        if k == 2:
                            if j+dj == n:
                                result[(k+1, next)].append( (k, curr))
                                valid_ends.append(next)
                        else:
                            result[(k+1, next)].append((k, curr))
                        
        
        print("valid ends = ", valid_ends)

        for k, v in result.items():
            print(k, v)


        results = []
        for end in valid_ends:
            curr = (3, end)
            k, c = curr

            r = [c]
            while k > 0:
                k, c = result[(k, c)][0]
                r.append(c)
            results.append(".".join(r[::-1]) )


        return results


if __name__ == '__main__':
    sol = Solution()

    input_list = [
        "25525511135",
        "11111"
    ]

    for inp in input_list:
        result = sol.restoreIpAddresses(inp)

        print(result)
        