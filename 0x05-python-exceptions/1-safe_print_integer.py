#!/usr/bin/python3
def safe_print_integer(value):
    is_number = True
    try:
        print("{:d}".format(int(value)))
    except ValueError:
        is_number = False
    finally:
        return is_number
