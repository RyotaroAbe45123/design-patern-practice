import sys

from hot_pot.pot import Pot
from hot_pot.hot_pot import HotPot

def main():
    want_to_eat = sys.argv[1]

    hot_pot: HotPot = HotPot(Pot())


if __name__ == "__main__":
    main()