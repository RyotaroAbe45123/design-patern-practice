from abc import ABCMeta, abstractmethod


class Vegetable(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass