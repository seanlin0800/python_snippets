""" A simplified version mimicking the built-in property class.

See https://docs.python.org/2/howto/descriptor.html
"""


class Property(object):

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset
        self.__name__ = fget.__name__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError('unreadable attribute')
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError('can not set attribute')
        self.fset(obj, value)

    def setter(self, fset):
        self.fset = fset
        return self


class Test(object):

    def __init__(self, name):
        self.__name = name

    @Property
    def name(self):
        return '{} in Test'.format(self.__name)

    @name.setter
    def name(self, name):
        if not isinstance(name, basestring):
            raise TypeError('name must be string')
        self.__name = name
