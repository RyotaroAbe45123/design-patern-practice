import sys

from factory import Factory
from hot_pot.pot import Pot
from hot_pot.hot_pot import HotPot


def main():
    assert len(sys.argv) != 1, "Argments Error"
    want_to_eat = sys.argv[1]

    factory: Factory = Factory.get_factory(want_to_eat)
    print(factory)

    hot_pot: HotPot = HotPot(Pot())
    hot_pot.add_soup(factory.get_soup())
    hot_pot.add_protain(factory.get_protain())
    hot_pot.add_vegetables(factory.get_vegetables())
    hot_pot.add_other_ingredients(factory.get_other_ingredients)


if __name__ == "__main__":
    main()