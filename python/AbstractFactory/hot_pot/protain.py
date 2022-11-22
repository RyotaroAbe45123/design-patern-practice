from abc import ABCMeta, abstractmethod


class Protain(metaclass=ABCMeta):
    @abstractmethod
    def get_protain(self):
        pass