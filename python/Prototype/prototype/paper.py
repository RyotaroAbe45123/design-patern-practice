from copy import deepcopy

from cloneable import Cloneable


class Paper(Cloneable):
    def __init__(self, name: str = None):
        if name is not None: self.__name = name

    def create_clone(self):
        new_paper = deepcopy(self)
        return new_paper