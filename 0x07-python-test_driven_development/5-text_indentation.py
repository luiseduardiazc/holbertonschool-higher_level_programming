#!/usr/bin/python3
"""Module text_indentation"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError('text must be a string')

    for i in ['.', '?', ':']:
        text = (i + '\n\n').join([row.strip(' ') for row in text.split(i)])

    print(text, end="")
