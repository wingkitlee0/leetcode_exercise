from typing import List, Deque, Tuple, Set
from collections import deque, defaultdict

"""
Given a list of list of characters, print out all the possible paths (strings) 
by walking horizontally and vertically along the cells. Each path only visit each
site once.

e.g., [[A, B], [C, D]] -> ['ABDC', 'ACDB']

"""

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
        pass

if __name__ == '__main__':
    input_list = [
        [  ['A','B','C','E'],  ['S','F','C','S'],  ['A','D','E','E']],
        [ ['A', 'B'], ['C', 'D']],
        [ ['A', 'B', 'C'], ['D', 'E', 'F']],
        [ ['A', 'B', 'C'] ]
    ]

    sol = Solution()
    for inp in input_list:
        result = sol.get_all_strings(board=inp)
        for r in result:
            print(r)