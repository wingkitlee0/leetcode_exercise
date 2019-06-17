"""
short path between top-left and bottom-right corners in 
a binary matrix (random?)
"""

import numpy as np 
import matplotlib.pyplot as plt

class BinaryMatrix:
    def __init__(self, N=5, fraction_one=0.3, **kwargs):
        self.N = N
        self.fraction_one = fraction_one
        self.matrix = self.gen_matrix(**kwargs)

    def gen_matrix(self, **kwargs):
        """
        fraction_one : 
        """

        entries = np.random.random_sample(self.N**2)

        matrix = np.zeros((self.N**2), dtype=int)
        matrix[entries<self.fraction_one] = 1

        matrix = matrix.reshape((self.N, self.N))

        # fixing the start and end points
        matrix[0,0] = 0
        matrix[-1,-1] = 0

        return matrix

def test():
    BM = BinaryMatrix(N=5,fraction_one=0.3)
    matrix = BM.gen_matrix()
    for row in matrix:
        print(row)

if __name__ == '__main__':
    test()








