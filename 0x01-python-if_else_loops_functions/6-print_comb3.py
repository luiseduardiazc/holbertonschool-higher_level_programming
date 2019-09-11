#!/usr/bin/python3

for numbers in range(1, 100):
    if numbers < 10:
        print("{:02d}".format(numbers), end=', ')
    elif int(str(numbers)[1:] + str(numbers)[:1]) > numbers:
        if numbers is not 89:
            print("{:02d}".format(numbers), end=', ')
        else:
            print("{:02d}".format(numbers), end='\n')
