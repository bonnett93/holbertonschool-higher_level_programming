#!/usr/bin/python3
def weight_average(my_list):
    average = 0
    if my_list:
        denominator = 0
        divisor = 0
        for tuple_pair in my_list:
            denominator += tuple_pair[0] * tuple_pair[1]
            divisor += tuple_pair[1]
        average = denominator / divisor
    return average
