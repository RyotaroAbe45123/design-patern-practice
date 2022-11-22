from abc import ABCMeta, abstractmethod


class Vegetable(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.vegetables = []

    def add(self, vegetable):
        self.vegetables.append(vegetable)

    @abstractmethod
    def get_vegetables(self):
        pass