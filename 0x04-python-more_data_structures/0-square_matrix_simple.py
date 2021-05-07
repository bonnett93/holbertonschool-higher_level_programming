#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = matrix.copy()
    for i in range(len(new_m)):
        new_m[i] = list(map(lambda x: x**2, new_m[i]))
    return new_m
