from abc import ABCMeta, abstractmethod

class Builder(metaclass=ABCMeta):
    @abstractmethod
    def add_solute(self):
        raise NotImplementedError

    @abstractmethod
    def add_solvent(self):
        raise NotImplementedError

    @abstractmethod
    def remove_solution(self):
        raise NotImplementedError

    @abstractmethod
    def get_concentration(self):
        raise NotImplementedError