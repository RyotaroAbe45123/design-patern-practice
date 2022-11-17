from abc import ABCMeta, abstractmethod

class Builder(metaclass=ABCMeta):
    @abstractmethod
    def add_solute(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_solvent(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_solution(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_concentration(self):
        raise NotImplementedError