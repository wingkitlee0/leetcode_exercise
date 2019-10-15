from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:

        if A == []:
            return []

        N = len(A)
        ie = 0
        io = 1
        #flag_odd = False; flag_even = False
        while (io <= N-1) and (ie <= N-2):
            print(io, ie)

            if A[io] % 2 == 1:
                io += 2
            
            if A[ie] % 2 == 0:
                ie += 2
            
            if A[io] % 2 == 0 and A[ie] % 2 == 1:
                print("swap {}, {} at ({}, {})".format(A[io], A[ie], io, ie))
                A[ie], A[io] = A[io], A[ie]
                ie += 2; io += 2
                
        return A

if __name__ == "__main__":

    #A = [4, 2, 5, 7]
    A = [4, 4, 4, 1, 1, 1]
    sol = Solution()

    result = sol.sortArrayByParityII(A)
    print(result)