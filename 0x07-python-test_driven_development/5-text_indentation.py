#!/usr/bin/python3
""" Text indentation module
"""


def text_indentation(text):
    """text_indentation function

        Args:
        text: string of texts
    """
    if not type(text) in [str]:
        raise TypeError("text must be a string")

    for c in range(len(text)):
        if text[c] in [".", "?", ":"]:
            if (c + 1) != len(text) and text[c+1] == " ":
                c += 1
                print(text[c-1], end="\n\n")
            else:
                print(text[c], end="\n\n")
        else:
            print(text[c], end="")
