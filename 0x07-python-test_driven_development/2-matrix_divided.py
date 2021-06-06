#!/usr/bin/python3
'''Module 2: matrix divided'''


def matrix_divided(matrix, div):
    '''divides all elements of a matrix and return new matrix'''
    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if type == 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    matrix_msg = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        new_row = []
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(matrix_msg)
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
