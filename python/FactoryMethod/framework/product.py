from abc import ABC, abstractmethod


class Product(metaclass=ABC):
    def print(self) -> None:
        print("-----")
        for i in range(5):
            self.draw()
            self.cut()
        print("-----")

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def cut(self) -> None:
        pass
