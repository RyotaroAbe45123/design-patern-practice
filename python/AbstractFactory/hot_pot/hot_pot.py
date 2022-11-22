from typing import List

from .pot import Pot
from .soup import Soup
from .protain import Protain
from .vegetable import Vegetable
from .ingredient import Ingredient


class HotPot:
    def __init__(self, pot: Pot) -> None:
        self.pot = pot

    def add_soup(self, soup: Soup) -> None:
        self.soup = soup

    def add_protain(self, protain: Protain) -> None:
        self.protain = protain
        
    def add_vegetables(self, vegetables: List[Vegetable]) -> None:
        self.vegetables = vegetables

    def add_other_ingredients(self, other_ingredients: List[Ingredient]) -> None:
        self.other_ingredients = other_ingredients