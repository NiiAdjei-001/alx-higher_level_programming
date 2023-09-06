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
    size = len(text)
    c = 0
    while c < size:
        if text[c] in [".", "?", ":"]:
            print(text[c], end="\n\n")
            while c < len(text)-1:
                if text[c + 1] == " ":
                    c += 1
                else:
                    break
        else:
            print(text[c], end="")
        c += 1
