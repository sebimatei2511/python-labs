# Exercitiul 9
# Write a function that receives as paramer a matrix which represents 
# the heights of the spectators in a stadium and will return 
# a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. 
# A spectator can't see the game if there is at least one taller spectator standing in front of him. 
# All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, 
# beginning with the closest row from the field.
# Example:
# FIELD
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 7, 2],
# [5, 5, 2, 5, 6, 4],
# [6, 6, 7, 6, 7, 5]] 
# Will return : [(2, 2), (3, 4), (2, 4)] 

def spectacle(matrix, m, n):
    result = []

    for j in range(0, n):
        maxim_on_row = 0
        for i in range(0, m):
            if matrix[i][j] > maxim_on_row:
                maxim_on_row = matrix[i][j]
            elif matrix[i][j] <= maxim_on_row:
                tuple = []
                tuple.append(i)
                tuple.append(j)
                result.append(tuple)

    return result
    
matrix = [[1, 2, 3, 2, 1, 1],
          [2, 4, 4, 3, 7, 2],
          [5, 5, 2, 5, 6, 4],
          [6, 6, 7, 6, 7, 5]]

print(spectacle(matrix, 4, 6))