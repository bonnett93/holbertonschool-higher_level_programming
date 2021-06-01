#!/usr/bin/python3


def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as f:
        characters = f.write(text)
    return characters
