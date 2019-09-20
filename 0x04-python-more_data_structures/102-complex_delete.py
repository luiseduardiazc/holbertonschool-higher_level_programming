#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = []
    list_items = a_dictionary.items()
    for item in list_items:
        if item[1] == value:
            list_keys.append(item[0])
    for key in list_keys:
        del a_dictionary[key]
    return a_dictionary
