#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or len(my_list) - 1 < idx:
        return my_list
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
    my_list.clear()
    for i in new_list:
        my_list.append(i)
    return my_list
