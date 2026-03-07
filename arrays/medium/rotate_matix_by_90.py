def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        a = 0
        b = n - 1
        while a < b:
            matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
            a += 1
            b -= 1