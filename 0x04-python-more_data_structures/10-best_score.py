#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_list = sorted(a_dictionary.items(),
                          key=lambda x: x[1], reverse=True)
        return new_list[0][0]
    return None
