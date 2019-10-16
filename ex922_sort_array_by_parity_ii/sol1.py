from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:

        if A == []:
            return []

        N = len(A)
        ie = 0
        io = 1
        flag_odd = False; flag_even = False
        while (io <= N-1) and (ie <= N-2):
            print(io, ie)

            if A[io] % 2 == 1:
                if not flag_odd:
                    io += 2
            else:
                flag_odd = True # lock

            if A[ie] % 2 == 0:
                if not flag_even:
                    ie += 2
            else:
                flag_even = True

            if flag_even and flag_odd:
                print("swap {}, {} at ({}, {})".format(A[io], A[ie], io, ie))
                A[ie], A[io] = A[io], A[ie]
                flag_odd = False
                flag_even = False
        return A

if __name__ == "__main__":

    #A = [4, 2, 5, 7]
    A = [4, 4, 4, 1, 1, 1]
    sol = Solution()

    result = sol.sortArrayByParityII(A)
    print(result)