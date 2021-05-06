#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_0, a_1 = 0, 0
    b_0, b_1 = 0, 0
    if len(tuple_a) > 0:
        a_0 = tuple_a[0]
    if len(tuple_a) > 1:
        a_1 = tuple_a[1]
    if len(tuple_b) > 0:
        b_0 = tuple_b[0]
    if len(tuple_b) > 1:
        b_1 = tuple_b[1]
    a = a_0 + b_0
    b = a_1 + b_1
    c = (a, b)
    return (c)
