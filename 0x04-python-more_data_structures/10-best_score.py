#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        score = max(sorted(a_dictionary.values()))
        for key, value in a_dictionary.items():
            if value == score:
                return key
