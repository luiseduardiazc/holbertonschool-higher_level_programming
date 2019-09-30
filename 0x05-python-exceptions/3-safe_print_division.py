#!/usr/bin/python3
def safe_print_division(a, b):
    retult = None
    try:
        retult = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(retult))
        return retult
