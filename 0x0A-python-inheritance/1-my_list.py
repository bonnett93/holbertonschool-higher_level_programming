#!/usr/bin/python3
'''File: 1 My List'''


class MyList(list):
    '''class MyList that inherits from list
    Public instance method:
        -def print_sorted(self):'''

    def print_sorted(self):
        '''Prints the list, but sorted (ascending sort)'''
        print(sorted(self))
