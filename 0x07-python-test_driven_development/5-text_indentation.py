#!/usr/bin/python3
"""4. Text indentation"""


def text_indentation(text):
    """ Text indentation """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    last_newline = False
    for idx in range(len(text)):
        if text[idx] == '.' or text[idx] == '?' or text[idx] == ':':
            print(text[idx])
            print()
            last_newline = True

        elif (text[idx] == ' ' or text[idx] == '\n') and last_newline:
            if text[idx] == '\n':
                print(text[idx], end="")
            continue
        else:
            last_newline = False
            print(text[idx], end="")
