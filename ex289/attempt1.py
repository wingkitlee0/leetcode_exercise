class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        Nx = len(board)
        Ny = len(board[0])


        for i in range(Nx):
            for j in range(Ny):
                numberOfLiveNeg = 1
                sign = 1 if board[i][j]==1 else -1
                for ioff in [-1,0,1]:
                    for joff in [-1,0,1]:
                        if i+ioff >=0 and i+ioff < Nx:
                            if j+joff >=0 and j+joff < Ny:
                                if board[i+ioff][j+joff] > 0 and not ioff==joff==0:
                                    numberOfLiveNeg += 1
                board[i][j] = numberOfLiveNeg*sign

        for i in range(len(board)):
            print(board[i])      

        for i in range(Nx):
            for j in range(Ny):
                print(i,j,board[i][j])
                if board[i][j] < 0:
                    if board[i][j] == -4: # originally dead, but with 3 live neighbor
                        print("1: ", board[i][j])
                        board[i][j] = 1
                    else:
                        print("2: ", board[i][j])
                        board[i][j] = 0 
                elif board[i][j] > 0:
                    if board[i][j] == 3 or board[i][j] == 4:
                        print("3: ", board[i][j])
                        board[i][j] = 1
                    else:
                        print("4: ", board[i][j])
                        board[i][j] = 0
                print("end: ", i,j,board[i][j])
                


if __name__=='__main__':
    M = [  [0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]
        ]
    sol = Solution()
    sol.gameOfLife(M)

    for i in range(len(M)):
        print(M[i])

