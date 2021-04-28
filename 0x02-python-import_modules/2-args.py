#!/usr/bin/python3
from sys import argv


def main():
    counter = len(argv) - 1
    if counter == 0:
        print("0 arguments.")
    if counter == 1:
        print("1 argument:")
    if counter > 1:
        print("{} arguments:".format(counter))
    for index, value in enumerate(argv):
        if index == 0:
            continue
        print("{}: {}".format(index, value))

if __name__ == "__main__":
    main()
