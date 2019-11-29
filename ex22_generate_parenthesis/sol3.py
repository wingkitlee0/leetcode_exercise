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
            s, r = res.pop(0) # s is the sum of 1, -1
            print(s, r)

            if len(r) < 2*n:
                res.append((s+1, r+["("]))
            if s > 0:
                res.append((s-1, r+[")"]))

            flag = all([len(r)==2*n for _, r in res])
        
        res = [ "".join(r[1]) for r in res if r[0]==0]
        return res

        # result = []
        # for r in res:
        #     #print(r)
        #     #s = ["(" if c == 1 else ")" for c in r]
        #     result.append("("+"".join(r)+")")

        # return result

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
        print(len(result), len(set(result)))