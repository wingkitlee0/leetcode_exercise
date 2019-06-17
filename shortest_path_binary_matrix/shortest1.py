"""
short path between top-left and bottom-right corners in 
a binary matrix (random?)
"""

import numpy as np 
import matplotlib.pyplot as plt

from collections import deque
import copy

from binarymatrix import BinaryMatrix

class ShortestPath:
    def find_shortest_path(self, matrix, diagonal=True):
        """
        find the shortest path using BFS

        Args:
            matrix : numpy matrix
            diagonal : True for allowing moving diagonally (via edges)
        """
        nx, ny = len(matrix[0]), len(matrix)
        print(nx, ny)

        current_level = [(0,0)]

        if diagonal:
            look_around = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0),
                (-1, -1), (0, -1), (1, -1)]
        else:
            # no diagonal
            look_around = [(1, 0), (0, 1), (-1, 0), (0, -1)]



        parents = {} # store all the parents, allow backtracking

        step = 0
        matrix[0, 0] = 1
        while current_level:
            moved = False
            next_level = []

            for i, j in current_level:
                print("current position ({:1d},{:1d}), step = {}".format(i,j, step))
                for di, dj in look_around:
                    i1, j1 = i+di, j+dj
                    if 0 <= i1 < nx and 0 <= j1 < ny and \
                        matrix[i1, j1] == 0:
                        # valid node to visit next step

                        # store the current (i,j) as parent of future node
                        parents[(i1,j1)] = (i, j) 

                        if i1 == nx-1 and j1 == ny-1:
                            # reaches the end point
                            step += 1
                            print("reach the end point!", step)
                            return step, parents

                        print("{} {} : {} ".format(i1, j1, matrix[i1, j1]))
                        next_level.append((i1, j1))
                        matrix[i1,j1] = 1

            current_level = next_level
            step += 1
        return -1, parents                     

def test_one():
    BM = BinaryMatrix(N=5,fraction_one=0.3)
    matrix = BM.gen_matrix()
    for row in list(matrix):
        print(row)
    

def test_two():
    #np.random.seed(1234)

    N = 8
    FRACTION = 0.35
    DIAGONAL = False

    BM = BinaryMatrix(N=N,fraction_one=FRACTION)
    matrix = BM.matrix

    grid = []
    for i in range(BM.N):
        grid.append(['X' if matrix[i,j] else 0 for j in range(BM.N)])
    
    mypath = ShortestPath()
    min_step, parents = mypath.find_shortest_path(matrix, diagonal=DIAGONAL)
    print("min step = {}".format(min_step))

    if min_step == -1:
        print("no path possible.")
    else:
        curr = (BM.N-1, BM.N-1)
        shortest_path = [curr]
        while curr != (0, 0):
            ic, jc = curr; ip, jp = parents[curr]
            print("({:1d},{:1d}) <- ({:1d},{:1d})".format(ic, jc, ip, jp))
            curr = parents[curr]
            shortest_path.insert(0, curr)   

        print(shortest_path)

    
    if min_step > 0:
        for i, j in shortest_path:
            grid[i][j] = '*'

    for row in grid:
        print("".join(["{:>2} ".format(x) for x in row]))


if __name__ == '__main__':
    #test_one()
    test_two()






