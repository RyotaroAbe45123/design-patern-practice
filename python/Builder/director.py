from builder import Builder

class Director:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def constract(self):
        self.builder.add_solvent(100)
        self.builder.add_solute(40)
        self.builder.remove_solution(70)
        self.builder.add_solvent(100)
        self.builder.add_solute(15)

    def get_result(self) -> float:
        return self.builder.get_concentration()
