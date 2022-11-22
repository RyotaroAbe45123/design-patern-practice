from abc import ABCMeta, abstractmethod


class Ingredient(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    @abstractmethod
    def get_ingredients(self):
        pass