from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ["()"]

        res = [(0, [])]
        flag = False
        while res != [] and not flag:
            # 1 for "(" and -1 for ")"
            s, r = res.pop(0) # s is the sum of 1, -1

            res.append((s+1, r+[1]))
            if s >= 0:
                res.append((s-1, r+[-1]))

            flag = all([len(r)==2*n-2 for _, r in res])
        
        res = [ r[1] for r in res if r[0]==0]
        
        result = []
        for r in res:
            #print(r)
            s = ["(" if c == 1 else ")" for c in r]
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
        print(len(result))
        print(len(set(result)))