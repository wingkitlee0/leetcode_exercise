"""
short path between top-left and bottom-right corners in 
a binary matrix (random?)
"""

import numpy as np 
import matplotlib.pyplot as plt

from collections import deque

from binarymatrix import BinaryMatrix

class ShortestPath:
    def find_shortest_path(self, matrix):
        """
        BFS
        """
        nx, ny = len(matrix[0]), len(matrix)
        print(nx, ny)

        current_level = [(0,0)]
        look_around = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0),
            (-1, -1), (0, -1), (1, -1)]

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
                        
                        if i1 == nx-1 and j1 == ny-1:
                            step += 1
                            print("reach the end point!", step)
                            return step

                        print("{} {} : {} ".format(i+di, j+dj, matrix[i+di, j+dj]))
                        next_level.append((i1, j1))
                        matrix[i1,j1] = 1

            current_level = next_level
            step += 1
        return -1                     

def test_one():
    BM = BinaryMatrix(N=5,fraction_one=0.3)
    matrix = BM.gen_matrix()
    for row in list(matrix):
        print(row)
    

def test_two():
    np.random.seed(12345)
    BM = BinaryMatrix(N=5,fraction_one=0.3)
    matrix = BM.gen_matrix()

    for row in list(matrix):
        print(row)
    
    mypath = ShortestPath()
    min_step = mypath.find_shortest_path(matrix)
    print("min step = {}".format(min_step))


if __name__ == '__main__':
    #test_one()
    test_two()








