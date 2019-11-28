from typing import List
from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        nwords = len(words)
        if nwords == 0:
            return 0
        if nwords == 1:
            return 1 if len(words[0]) == 1 else 0
        
        words.sort(key=len)
#        print(words)

        d = defaultdict(int)

        for word in words:
            if len(word) == 1:
                d[word] = 1
            else:
                for i in range(len(word)):
                    pre_word = word[:i] + word[i+1:]
                    print(pre_word, end=" ")
                    if pre_word in d:
                        print(".", end=" ")
                        if d[pre_word] + 1 > d[word]:
                            d[word] = d[pre_word] + 1
                    else:
                        if d[word] == 0:
                            d[word] = 1

                print(" stored: ", word, d[word])
                        

        for k, v in d.items():
            print(k, v)

        if len(d.values()) == 0:
            return 0
        else:
            return max(d.values())

    def longestStrChain_(self, words: List[str]) -> int:
        nwords = len(words)
        if nwords == 0:
            return 0
        if nwords == 1:
            return 1 if len(words[0]) == 1 else 0
        
        words.sort(key=len)
#        print(words)

        d = defaultdict(int)

        for word in words:
            if len(word) == 1:
                d[word] = 1
            else:
                for i in range(len(word)):
                    pre_word = word[:i] + word[i+1:]
                    #print(pre_word)
                    if pre_word in d:
                        d[word] = d[pre_word] + 1

        # for k, v in d.items():
        #     print(k, v)

        if len(d.values()) == 0:
            return 0
        else:
            return max(d.values())

if __name__ == '__main__':

    input_list = [
        ["a","b","ba","bca","bda","bdca"],
        ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"] # expect 7
    ]

    sol = Solution()

    for inp in input_list:
        result = sol.longestStrChain(inp)
        print(result)

        