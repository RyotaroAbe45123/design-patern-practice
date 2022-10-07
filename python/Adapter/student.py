class Student:
    def __init__(self, name: str) -> None:
        self.name = name


    def call(self):
        print(f"I am student: {self.name}.")