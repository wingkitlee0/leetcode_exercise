class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 10:
            return [s]
        else:

            words = [s[i:i+10] for i in range(len(s)-9)]

            count_dict = {}
            for w in words:
                if w in count_dict:
                    count_dict[w] += 1
                else:
                    count_dict[w] = 1

            result = []
            for k, v in count_dict.items():
                if v > 1:
                    result.append(k)
            return result

    def words2number(self, words):
        numbers = []
        for word in words:
            number = 0
            for i, w in enumerate(word):
                number += int(self._dict[w]) * 4**i
            numbers.append(number)
        return numbers



    
if __name__ == '__main__':
    sol = Solution()
    
    res = sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

    print(res)

    print(sol.findRepeatedDnaSequences("AAAAAAAAAA"))