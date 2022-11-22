from abc import ABCMeta, abstractmethod


class Soup(metaclass=ABCMeta):
    @abstractmethod
    def get_soup(self):
        pass