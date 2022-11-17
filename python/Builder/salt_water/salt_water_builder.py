from builder import Builder
from .salt_water import SaltWater


class SaltWaterBuilder(Builder):
    def __init__(self) -> None:
        self._salt_water = SaltWater(0, 0)

    def add_solute(self, solute_amount: int) -> None:
        self._salt_water.salt += solute_amount

    def add_solvent(self, solvent_amount: int) -> None:
        self._salt_water.water += solvent_amount

    def remove_solution(self, solution_amount: int) -> None:
        self._salt_water.salt -= solution_amount * (self._salt_water.salt / (self._salt_water.salt + self._salt_water.water))
        self._salt_water.water -= solution_amount * (self._salt_water.water / (self._salt_water.salt + self._salt_water.water))

    def get_concentration(self) -> float:
        return self._salt_water.salt / (self._salt_water.salt + self._salt_water.water)