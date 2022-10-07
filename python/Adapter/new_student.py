from chair_person import ChairPerson
from student import Student


class NewStudent(ChairPerson, Student):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def control_class(self) -> None:
        print("I can control class.")
        self.call()