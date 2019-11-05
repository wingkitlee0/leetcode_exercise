from typing import List
from collections import defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        d = defaultdict(int)
        for c in chars:
            d[c] += 1

        r = 0
        for word in words:
            d_ = d.copy()
            i = 0
            while i < len(word):
                if d_[word[i]] > 0:
                    d_[word[i]] -= 1
                    i += 1
                else:
                    break

            if i == len(word):
                r += len(word)

        return r



if __name__ == '__main__':
    input_list = [
        {'words': ["cat","bt","hat","tree"], 'chars': "atach"},
        {'words': ["hello","world","leetcode"], 'chars': "welldonehoneyr"}
    ]

    sol = Solution()

    for inp in input_list:
        result = sol.countCharacters(**inp)
        print(result)