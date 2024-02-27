#!/usr/bin/python3
"""Square Module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """To string method"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """Return size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square with *args => id, size, x, y"""
        if (args and args is not None):
            if args.__len__() > 0:
                self.id = args[0]
            if args.__len__() > 1:
                self.width = args[1]
                self.height = args[1]
            if args.__len__() > 2:
                self.x = args[2]
            if args.__len__() > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs.keys():
                self.id = kwargs['id']
            if 'size' in kwargs.keys():
                self.width = kwargs['size']
                self.height = kwargs['size']
            if 'x' in kwargs.keys():
                self.x = kwargs['x']
            if 'y' in kwargs.keys():
                self.y = kwargs['y']

    def to_dictionary(self):
        """return a dictionary object of class instance"""
        dictionary = dict(
            id=self.id,
            size=self.width,
            x=self.x,
            y=self.y
        )
        return dictionary
