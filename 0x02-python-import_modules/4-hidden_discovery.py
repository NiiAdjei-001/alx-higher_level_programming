#!/usr/bin/python3
if __name__ == "__main__":
    from fnmatch import fnmatch
    pyc_path = "hidden_4.pyc"
    attribute_list = dir(pyc_path)
    for element in attribute_list:
        if not fnmatch(element,'__*'):
            print(element)
