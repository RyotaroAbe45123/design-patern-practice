from abstract import AbstractClass

class ConcreteB(AbstractClass):
    def __init__(self) -> None:
        self.number = 0

    def prepare(self) -> None:
        print(f"started by B: {self.number}")

    def draw(self) -> None:
        self.number += 1
        print(f"draw (plus 1): {self.number}")

    def cut(self) -> None:
        self.number -= 1
        print(f"cut (minus 1): {self.number}")
