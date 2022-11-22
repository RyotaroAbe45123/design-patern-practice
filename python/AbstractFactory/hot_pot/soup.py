from abc import ABCMeta, abstractmethod


class Soup(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass