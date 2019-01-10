class Solution:
    _dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = [s[i:i+10] for i in range(len(s)-10)]
        print(words)

        numbers = self.words2number(words)
        print(numbers)

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
    
    sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

    print(sol.words2number(['AAAG']))