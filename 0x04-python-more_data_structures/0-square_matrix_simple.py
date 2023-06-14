#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = matrix.copy()
    for line in range(len(matrix)):
        matrix_2[line] = list(map((lambda x: x**2), matrix[line]))
    return (matrix_2)
