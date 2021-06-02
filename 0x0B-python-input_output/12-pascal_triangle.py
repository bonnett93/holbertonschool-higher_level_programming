#!/usr/bin/python3
'''File: 12 pascal'''


def pascal_triangle(n):
    '''returns a list of lists of integers
    representing the Pascal’s triangle of n'''
    if n<=0:
        return []

    triangle= [[1]]
    for i in range(0,n-1):
        tmp = [0] + triangle[i] + [0]
        subtriangle = []
        for j in range(len(tmp) - 1):
            subtriangle.append(tmp[j] + tmp[j + 1])
        triangle.append(subtriangle)
    return(triangle)


