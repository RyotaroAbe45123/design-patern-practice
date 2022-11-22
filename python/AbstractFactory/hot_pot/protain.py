from abc import ABCMeta, abstractmethod


class Protain(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass