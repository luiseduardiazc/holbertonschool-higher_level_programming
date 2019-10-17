#!/usr/bin/python3
""" Script that adds all arguments to a Python list
    and then save them to a file """
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []
argv = sys.argv

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    with open(filename, 'w') as file:
        pass
finally:
    for ar in argv[1:]:
        my_list.append(ar)

save_to_json_file(my_list, filename)
