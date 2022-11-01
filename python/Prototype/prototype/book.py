from copy import deepcopy

from cloneable import Cloneable


class Book(Cloneable):
    def __init__(self):
        self.__name = "book"

    def create_clone(self):
        new_book = deepcopy(self)
        return new_book