from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def draw(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def cut(self) -> None:
        raise NotImplementedError()

    def print(self) -> None:
        self.prepare()
        print("-----")
        for i in range(5):
            self.draw()
            self.cut()
        print("-----")
        print("-----")
