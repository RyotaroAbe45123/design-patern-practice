from typing import List

from factory import Factory
from hot_pot.vegetable import Vegetable
from hot_pot.ingredient import Ingredient
from .chicken_bones_soup import ChickenBonesSoup
from .chicken import Chicken
from .chinese_cabbage import ChineseCabbage
from .leek import Leek
from .chrysanthemum import Chrysanthemum
from .tofu import Tofu


class MizutakiFactory(Factory):
    def get_soup(self):
        return ChickenBonesSoup()

    def get_protain(self):
        return Chicken()

    def get_vegetables(self):
        vegetables: List[Vegetable] = []
        vegetables.append(ChineseCabbage())
        vegetables.append(Leek())
        vegetables.append(Chrysanthemum())
        return vegetables

    def get_other_ingredients(self):
        ingredients: List[Ingredient] = []
        ingredients.append(Tofu())
        return ingredients