#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_results = []
    try:
        for index in range(0, list_length):
            try:
                list_results.append(my_list_1[index] / my_list_2[index])
            except (TypeError, ValueError):
                list_results.append(0)
                print("wrong type")
            except ZeroDivisionError:
                list_results.append(0)
                print("division by 0")
    except IndexError:
        list_results.append(0)
        print("out of range")
    finally:
        return list_results
