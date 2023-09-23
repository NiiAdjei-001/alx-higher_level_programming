#!/usr/bin/python3
"""Base Model Module
"""


class Base:
    """Bass Class
    """
    __nb_object = 0
    """Number of object instances"""

    def __init__(self, id=None):
        """Init Method

            Arg:
                id: (optional) id for object instance
        """
        if (id is None):
            type(self).__nb_object += 1
            self.id = self.__nb_object
        else:
            # type(self).__nb_object += 1
            self.id = id
