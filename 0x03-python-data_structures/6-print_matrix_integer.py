#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for vector in matrix:
        x = len(vector)
        for i, value in enumerate(vector):
            if i != x - 1:
                print("{:d}".format(value), end=" ")
            else:
                print("{:d}".format(value))
    if x == 0:
        print("")
