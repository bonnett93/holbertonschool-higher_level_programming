#!/usr/bin/python3
"""Module: 6-peak.py"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    sort_list = list_of_integers.sort()
    return (sort_list[-1])
