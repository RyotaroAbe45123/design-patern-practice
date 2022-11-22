from hot_pot.protain import Protain


class Chicken(Protain):
    def get_protain(self) -> Protain:
        return Chicken()