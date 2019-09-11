#!/usr/bin/python3
def uppercase(str):
    str = list(str)
    for index in range(0, len(str)):
        if ord(str[index]) in range(97, 123):
            str[index] = chr(ord(str[index]) - 32)
    print("{}".format("".join(str)))
