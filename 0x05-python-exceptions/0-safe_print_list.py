#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    try:

        for i in range(x):
            print("{}".format(my_list[x]), end="")
            elements += 1
    except:
        pass
    finally:
        return elements
