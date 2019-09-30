#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for index in range(0, x):
            print("{}".format(my_list[index]), end='')
            count += 1
    except expression as identifier:
        pass
    finally:
        print()
        return count
