from abc import ABCMeta, abstractmethod


class Ingredient(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass