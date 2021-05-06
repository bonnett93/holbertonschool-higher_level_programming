#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 1:
        for vector in matrix:
            for i in range(0, len(vector) - 1):
                print("{:d}".format(vector[i]), end=" ")
            print("{:d}".format(vector[-1]))
    else:
        print("")
