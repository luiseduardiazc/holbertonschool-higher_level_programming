#!/usr/bin/python3
def remove_char_at(str, n):
    str = list(str)
    try:
        if n >= 0:
            del str[n]
    except Exception as e:
        return "".join(str)

    return "".join(str)
