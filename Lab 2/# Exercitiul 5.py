# Exercitiul 5
# Write a function that receives as parameter a matrix and will 
# return the matrix obtained by replacing all the elements under 
# the main diagonal with 0 (zero).

def rebuild_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i > j:
                matrix[i][j] = 0

    return matrix

matrix_input = [[1,2,3],[4,5,6],[7,8,9]]

print(rebuild_matrix(matrix_input))