#rotate matrix by 90 degrees
def rotate(matrix , N):
        for i in range(N):
            for j in range(i):
                matrix[i][j] , matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        
