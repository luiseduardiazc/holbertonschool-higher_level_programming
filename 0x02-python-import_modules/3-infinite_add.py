#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    len_argv = len(argv)

    def add_arguments(argv):
        sum_arguments = 0
        for argument in argv[1:]:
            sum_arguments += int(argument)
        return sum_arguments

    if len_argv is 1:
        print(0)
    else:
        print("{:d}".format(add_arguments(argv)))
