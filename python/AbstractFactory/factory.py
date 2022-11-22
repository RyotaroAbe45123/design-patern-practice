from abc import ABCMeta, abstractmethod
from typing import List

from hot_pot.soup import Soup
from hot_pot.protain import Protain
from hot_pot.vegetable import Vegetable
from hot_pot.ingredient import Ingredient


class Factory(metaclass=ABCMeta):
    @staticmethod
    def get_factory(factory_name: str) -> None:
        # グローバルにインポートすると循環参照になるので、関数内でインポート
        from mizutaki.mizutaki_factory import MizutakiFactory
        if factory_name == "MizutakiFactory":
            pass
        else:
            raise Exception
        return eval(factory_name)()

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