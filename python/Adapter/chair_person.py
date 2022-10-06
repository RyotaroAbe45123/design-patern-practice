from abc import ABCMeta, abstractmethod


class ChairPerson(metaclass=ABCMeta):
    @abstractmethod
    def control_class(self) -> None:
        raise NotImplementedError()