from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ["()"]

        i = 0
        res = [(0, [])]
        flag = False
        while res != [] and not flag:
            cnt, r = res.pop(0)
            res.append((cnt, r+[0]))
            if cnt+1 < n:
                res.append((cnt+1, r+[1]))
            #print(res)

            i += 1
            flag = all([len(r)==2*n-2 for _, r in res])
        
        if n > 2:
            res = [ r[1] for r in res if r[0]==n-1 and sum(r[1][n-1:]) > 0]
        else:
            res = [ r[1] for r in res if r[0]==n-1]

        result = []
        for r in res:
            #print(r)
            s = ["(" if c == 0 else ")" for c in r]
            result.append("("+"".join(s)+")")

        return result

if __name__ == "__main__":

    input_list = [
        0,
        1,
        2,
        3,
        4,
    ]

    sol = Solution()
    for inp in input_list:
        result = sol.generateParenthesis(n=inp)
        print(result)