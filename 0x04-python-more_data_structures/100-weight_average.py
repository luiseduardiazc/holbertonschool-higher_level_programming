#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    def mult_items(x, y): return x*y
    result_sum_list_mult = sum(
        [mult_items(item[0], item[1]) for item in my_list])

    result_sum_list = sum([item[1] for item in my_list])

    return result_sum_list_mult / result_sum_list
