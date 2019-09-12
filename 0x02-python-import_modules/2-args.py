#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    len_argv = len(argv)

    def print_num_arguments(num, message):
        print("{:d} {}".format(num, message))

    def print_arguments(argv):
        for argument in argv[1:]:
            print("{:d}: {}".format(argv.index(argument), argument))

    if len_argv is 1:
        print_num_arguments(len_argv - 1, "arguments.")
    elif len_argv is 2:
        print_num_arguments(len_argv - 1, "argument:")
        print_arguments(argv)
    else:
        print_num_arguments(len_argv - 1, "arguments.")
        print_arguments(argv)
