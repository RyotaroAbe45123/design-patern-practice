from typing import List

from pot import Pot

class HotPot:
    def __init__(self, pot: Pot) -> None:
        self.pot = pot

    def add_soup(self, soup: Soup) -> None:
        self.soup = soup

    def add_main(self, main: Main) -> None:
        self.main = main
        
    def add_vegetables(self, vegetables: List[Vegetables]) -> None:
        self.vegetables = vegetables

    def add_other_ingredients(self, other_ingredients: List[Ingredients]) -> None:
        self.other_ingredients = other_ingredients