# Exercitiul 5
# Given a square matrix of characters write a script that prints the string 
# obtained by going through the matrix in spiral order (as in the example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp      10 9  8  7

def spiral_way(rows,columns,matrix):

    row_index = 0
    column_index = 0

    while (row_index < rows and column_index < columns):
        
        # Afisam prima linie
        for i in range(column_index,columns):
            print(matrix[row_index][i], end='')
        row_index = row_index + 1

        # Afisam ultima coloana fara primul element
        for i in range(row_index,rows):
            print(matrix[i][rows-1], end='')
        columns = columns - 1

        # Afisam ultima linie de la dreapta la stanga
        for i in range(columns - 1, column_index - 1, -1):
            print(matrix[rows - 1][i], end='')
        rows = rows -1

        # Afisam prima coloana de jos in sus
        for i in range(rows - 1, row_index - 1, -1):
            print(matrix[i][column_index], end='')
        column_index = column_index + 1

matrix = [['f', 'i', 'r', 's'],
          ['n', '_', 'l', 't'],
          ['o', 'b', 'a', '_'],
          ['h', 't', 'y', 'p']]

spiral_way(4,4,matrix)
