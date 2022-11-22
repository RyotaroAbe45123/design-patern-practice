from abc import ABCMeta, abstractmethod
from typing import List

from hot_pot.soup import Soup
from hot_pot.protain import Protain
from hot_pot.vegetable import Vegetable
from hot_pot.ingredient import Ingredient


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def get_soup(self) -> Soup:
        pass

    @abstractmethod
    def get_protain(self) -> Protain:
        pass

    @abstractmethod
    def get_vegetables(self) -> List[Vegetable]:
        pass

    @abstractmethod
    def get_other_ingredients(self) -> List[Ingredient]:
        pass