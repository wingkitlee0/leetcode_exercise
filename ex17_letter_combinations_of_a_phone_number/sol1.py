from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.str_dict = defaultdict(list,)
        for i in range(26):
            c = chr(i+ord('a'))
            n = i//3+2
            if c not in ['s', 'v', 'y', 'z']:
                self.str_dict[n].append(c)
        self.str_dict[7].append('s')
        self.str_dict[8].append('v')
        self.str_dict[9].append('y')
        self.str_dict[9].append('z')
    
#        for k, v in self.str_dict.items():
#            print(k, v)


    def letterCombinations(self, digits: str) -> List[str]:

        ndigits = len(digits)
        if ndigits == 0:
            return []
        if ndigits == 1:
            return self.str_dict[int(digits[0])]

        result = [""]
        l = 0
        for d in digits:
            nresult = len(result)
            for i in range(nresult):
                r = result.pop(0)
                for c in self.str_dict[int(d)]:
                    result.append( r+str(c))
        
        return result

if __name__ == '__main__':

    input_list = [
        "23", 
        "",
        "2",
        "234"
    ]

    sol = Solution()
    for inp in input_list:
        result = sol.letterCombinations(inp)
        print(result)