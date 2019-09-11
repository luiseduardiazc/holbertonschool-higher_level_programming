#!/usr/bin/python3
def is_odd(num):
    if num % 2 == 0:
        return num
    return num - 32

for num in reversed(range(97, 123)):
        index = is_odd(num)
        print("{}".format(chr(index)), end='')
