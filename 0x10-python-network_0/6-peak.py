#!/usr/bin/python3
"""Module: 6-peak.py"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    return (sorted(list_of_integers)[-1])
