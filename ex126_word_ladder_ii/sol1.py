from typing import List, Dict, Set

class Solution:
    def compare(self, w1, w2):
        """
        compute the number of miss-matched characters
        """
        if len(w1) != len(w2):
            return -1

        miss_match = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                miss_match += 1
        return miss_match

    def get_word_graph(self, wordList: List[str]) -> Dict[str, Set]:
        """
        compute a graph based on the word list
        """
        word_set = set(wordList)
        word_graph = {}
        for w in word_set:
            word_graph[w] = set()
            for w_ in word_set:
                if w != w_:
                    if self.compare(w, w_) == 1:
                        word_graph[w].add(w_)
        return word_graph

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return [[]]

        word_graph = self.get_word_graph(wordList)
                
        for k, v in word_graph.items():
            print(k, v)

        queue = [[w] for w in word_graph if self.compare(w, beginWord) == 1]
        queue.sort(key=lambda w: len(word_graph[w[0]]))
        print("queue = {}".format(queue))
        paths = []

        maxlength = float('inf')
        while queue:
            curr = queue.pop(0)

            if curr[-1] == endWord and len(curr) < maxlength:
                path = [beginWord]+curr
                paths.append(path)
                if maxlength == float('inf'):
                    maxlength = len(path)

            if curr[-1] in word_graph:
                for w in word_graph[curr[-1]]:
                    if w not in curr:
                        queue.append( curr+[w])
       
        
        #print(beginWord, endWord, wordList)
        
        return paths




if __name__ == "__main__":
    
    input_list = [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"]),
        ("qa", "sq", 
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])
    ]

    sol = Solution()

    for inp in input_list:
        result = sol.findLadders(*inp)

        for r in result:
            print(r)