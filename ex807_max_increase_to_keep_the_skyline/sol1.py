from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        nx = len(grid) # rows
        if nx > 0:
            ny = len(grid[0]) # columns

        x_skyline = [max(grid[i]) for i in range(ny)]
        
        y_skyline = [max([grid[j][i] for j in range(ny)]) for i in range(nx)]
        print(x_skyline, y_skyline)

        #new_grid = [[min(x_skyline[i], y_skyline[j]) for j in range(ny)] for i in range(nx)]
        new_grid = [[min(x_skyline[i], y_skyline[j]) - grid[i][j] for j in range(ny)] for i in range(nx)]

        print(new_grid)

        return sum([sum(row) for row in new_grid])



if __name__ == '__main__':
    sol = Solution()
    result = sol.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
    print(result)