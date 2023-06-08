#!/usr/bin/python3
if __name__ == "__main__":
    from fnmatch import fnmatch
    import hidden_4
    attribute_list = dir(hidden_4)
    for element in attribute_list:
        if not fnmatch(element, '__*__'):
            print(element)
