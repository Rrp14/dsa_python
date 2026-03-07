"""better approach"""
class Solution:
    # Function to set entire row and column to 0 if an element in the matrix is 0
    def setZeroes(self, matrix):
        # Get number of rows
        m = len(matrix)
        # Get number of columns
        n = len(matrix[0])

        # Create row marker array
        row = [0] * m
        # Create column marker array
        col = [0] * n

        # First pass: mark rows and columns that need to be zeroed
        for i in range(m):
            for j in range(n):
                # If element is zero, mark its row and column
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        # Second pass: set cells to zero based on markers
        for i in range(m):
            for j in range(n):
                # If the row or column is marked, set cell to zero
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0

# Driver code



"""brute force"""
def setzeroes_bf(matrix):
    m=len(matrix)
    n=len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:

                for col in range(n):
                    if matrix[i][col]!=0:
                        matrix[i][col]=-1

                for row in range(m):
                    if matrix[row][j]!=0:
                        matrix[row][j]=-1


    for i in range(m):
        for j in range(n):
            if matrix[i][j]==-1:
                matrix[i][j]=0




"""optimal"""

def set_zero(matrix):
    m=len(matrix)
    n=len(matrix[0])

    is_row_zero=False
    is_col_zero=False

    for j in range(n):
        if matrix[0][j]==0:
            is_row_zero=True
            break


    for i in range(m):
        if matrix[i][0]==0:
            is_col_zero=True
            break


    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0


    for i in range(m):
        for j in range(n):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0


    if is_col_zero:
        for i in range(m):
            matrix[i][0]=0

    if is_row_zero:
        for j in range(n):
            matrix[0][j]=0




matris = [[1,1,1],[1,0,1],[1,1,1]]
set_zero(matris)
for r in matris:
    print(r)