#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def get_last_digit(number):
    if number < 0:
        number = number * - 1
        return (number % 10) * -1
    return number % 10

last_digit = get_last_digit(number)
message = "Last digit of {:d} is {:d}".format(number, last_digit)

if last_digit is 0:
    print("{} and is {:d}".format(message, last_digit))
elif last_digit > 5:
    print("{} and is greater than 5".format(message))
elif last_digit < 6:
    print("{} and is less than 6 and not 0".format(message))
