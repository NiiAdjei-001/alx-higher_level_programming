#!/usr/bin/python3
"""My List Module"""


class MyList(list):
    """
    """
    def __init__(self, ls=[]):
        super().__init__(ls)

    def print_sorted(self):
        """Returns  a list of available attributes and methods of an object
        """
        self.sort()
        print(self.__str__())
