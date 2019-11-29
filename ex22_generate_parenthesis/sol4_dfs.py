from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []

        def dfs(l, r, s):
            """
            Args:
                l: number of "("
                r: number of ")"
                s: current string
            """
            if len(s) == n*2: # max length
                self.result.append(s)
            if l < n: # add more "(" 
                dfs(l+1, r, s+"(")
            if r < l: # add more ")" 
                dfs(l, r+1, s+")")
        dfs(0,0,"")
        return self.result
        
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