#!/usr/bin/python3
'''Module 5: text indentation'''


def text_indentation(text):
    '''prints a text with 2 new lines after each of
        these characters: ., ? and :'''
    if type(text) != str:
        raise TypeError("text must be a string")

    if text[0] != " ":
        print(text[0], end="")
    for i in range(1, len(text)):
        if (text[i-1] in ".?:"):
            print("\n")
            if (text[i] == " "):
                continue
        print(text[i], end="")
