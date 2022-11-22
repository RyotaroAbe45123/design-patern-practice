from hot_pot.soup import Soup


class ChickenBonesSoup(Soup):
    def get_soup(self) -> Soup:
        return ChickenBonesSoup()