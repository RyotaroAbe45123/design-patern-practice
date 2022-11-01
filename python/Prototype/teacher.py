from typing import List
from time import sleep

from prototype.paper import Paper
from cloneable import Cloneable


class Teacher:
    def __init__(self):
        self.__showcase: dict = dict()

    def register(self, name: str, prototype: Cloneable):
        self.__showcase[name] = prototype

    def create_many_crystals(self, name: str):
        prototype: Cloneable = self.__showcase.get(name)
        assert prototype is not None, "Not Found this name prototype. So register it."

        self.draw_crystal(prototype)
        self.cut_accordance_with_line(prototype)

        papers: List[Paper] = [prototype.create_clone() for _ in range(100)]

        return papers

    def draw_crystal(self, prototype: Cloneable):
        print(f"{prototype}: drawing started.")
        sleep(5)
        print(f"{prototype}: drawing finished.")

    def cut_accordance_with_line(self, prototype: Cloneable):
        print(f"{prototype}: cutting started.")
        sleep(5)
        print(f"{prototype}: cutting finished.")
