from typing import List, Deque, Tuple, Set
from collections import deque, defaultdict

class Solution:
    def get_neighbors(self, board: List[List[str]], i: int, j: int) -> Deque[Tuple[int, int]]:
        neightbors = deque()
        nx = len(board); ny = len(board[0])

        if j < ny-1: # except right-most col
            neightbors.append( (i, j+1)) 
        if j > 0: # except left-most col
            neightbors.append( (i, j-1))
        if i > 0: # except top row
            neightbors.append( (i-1, j))
        if i < nx-1: # except bottom row
            neightbors.append( (i+1, j))

        return neightbors


    def get_all_strings(self, board: List[List[str]]) -> List[str]:

        i = 0
        j = 0
        queue = deque()
        queue.append((i, j, {(i, j): 0}))
        
        result = []

        while queue:
            i_, j_, d_ = queue.pop()

            nb_dict = self.get_neighbors(board, i_, j_) 

            nb_added = 0 # number of neighbors added
            while nb_dict:
                k, l = nb_dict.pop()
                if (k, l) not in d_:
                    new_d = d_.copy()
                    new_d[(k, l)] = len(d_)
                    queue.append( (k, l, new_d) )
                    nb_added += 1
        
            print(board[i_][j_], i_, j_, d_, nb_added)

            if nb_added == 0:
                # no nb added means the end of path
                char_list = [board[k[0]][k[1]] for k, v in d_.items()]
                print(char_list)
                result.append("".join(char_list))

        print()

        return result

    def exist(self, board: List[List[str]], word: str) -> bool:

        graph = {}
        dictionary = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                graph[(i, j)] = self.get_neighbors(board, i, j)
                dictionary[board[i][j]].append((i,j))

        
        print("graph:")
        for k, v in graph.items():
            print(board[k[0]][k[1]], [board[x[0]][x[1]] for x in v])

        print("dictionary")
        for k, v in dictionary.items():
            print(k, v)
        

        if len(word) == 0:
            return False
        if word[0] not in dictionary:
            return False

        stack = deque()
        for node in dictionary[word[0]]:
            seen = set()
            seen.add( (node[0], node[1]))
            stack.append( (node[0], node[1], 0, seen))

        while stack:
            i, j, k, seen = stack.pop()
            if k == 0:
                print("start: ")
            
            print(board[i][j], i, j, seen, stack)
            if k == len(word)-1:
                return True

            for node in graph[(i, j)]:
                if node not in seen and board[node[0]][node[1]] == word[k+1]:
                    seen_ = seen.copy()
                    seen_.add(node)
                    stack.append( (node[0], node[1], k+1, seen_))


            

        print(stack)






        return False

        
if __name__ == '__main__':
    input_list = [
        [['A', 'B', 'C', 'A'], ['D', 'A', 'E', 'F']]
        # [  ['A','B','C','E'],  ['S','F','C','S'],  ['A','D','E','E']],
        # [ ['A', 'B'], ['C', 'D']],
        # [ ['A', 'B', 'C'], ['D', 'E', 'F']],
        # [ ['A', 'B', 'C'] ]
    ]

    word_list = [
        'AF'
    ]

    sol = Solution()
    for board in input_list:
        
        for word in word_list:
            result = sol.exist(board, word)
            print(result)