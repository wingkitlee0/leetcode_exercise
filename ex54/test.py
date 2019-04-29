class Solution:
    def spiralOrder(self, matrix):
        if matrix is None:
            return None
        if matrix == []:
            return None
        
        nr = len(matrix)
        nc = len(matrix[0])
        
        if nr == 1:
            return matrix[0]
        if nc == 1:
            return [x[0] for x in matrix]
    
        lst = []
        for i in range( (nr+1)//2):
            # top: right
            if nc > 2*i:
                for j in range(i, nc-i):
                    lst.append(matrix[i][j])

            if len(lst) >= nr*nc:
                break

            # right: down
            for k in range(i+1, nr-i-1):
                lst.append(matrix[k][nc-i-1])

            if len(lst) >= nr*nc:
                break
            
            if nc > 2*i:
                for j in range(i, nc-i):
                    lst.append(matrix[nr-i-1][nc-1-j])
            
            if len(lst) >= nr*nc:
                break

            # left: up
            for k in range(i+1, nr-i-1):
                print(k, i, nr-1-k)
                lst.append(matrix[nr-1-k][i])
                
            if len(lst) >= nr*nc:
                break

        return lst

        


if __name__ == '__main__':
    sol = Solution()

    m1 = [
        [ 1, 2, 3, 4 ],
        [ 10, 11, 12, 5 ],
        [ 9, 8, 7, 6 ],
        [ 9, 8, 7, 6 ],
        [ 9, 8, 7, 6 ]
        ]
    sol.spiralOrder(m1)

    m2 = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]

    r = sol.spiralOrder(m2)
    print(r)

