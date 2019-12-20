from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ni, nj = len(grid), len(grid[0])
        
        number_of_islands = 0

        for j1 in range(nj):
            for i1 in range(ni):
                # (i1, j1) is the starting point
                if grid[i1][j1] == "1":
                    grid[i1][j1] = "S"
                    print("({:1d},{:1d})".format(i1,j1))

                    number_of_islands += 1

                    # below code is basically BFS
                    queue = deque()
                    queue.append( (i1,j1))
                    while queue:
                        i, j = queue.popleft()
                        if j < nj-1 and grid[i][j+1] == "1": # except right-most col
                            grid[i][j+1] = "S"
                            queue.append( (i, j+1)) 
                        if j > 0 and grid[i][j-1] == "1": # except left-most col
                            grid[i][j-1] = "S"
                            queue.append( (i, j-1))
                        if i > 0 and grid[i-1][j] == "1": # except top row
                            grid[i-1][j] = "S"
                            queue.append( (i-1, j))
                        if i < ni-1 and grid[i+1][j] == "1": # except bottom row
                            grid[i+1][j] = "S"
                            queue.append( (i+1, j))
        return number_of_islands

if __name__ == "__main__":
    input_list = [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","1"],
            ["1","1","0","1","0"]
        ],
        [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
    ]

    sol = Solution()
    for grid in input_list:
        result = sol.numIslands(grid)

        print("result = {}".format(result))
        
        for row in grid:
            print(row)