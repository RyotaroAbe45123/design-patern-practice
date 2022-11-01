from teacher import Teacher
from prototype.paper import Paper


def main():
    teacher = Teacher()

    paper = Paper("paper")

    teacher.register("paper", paper)

    teacher.create_many_crystals("paper")


if __name__ == "__main__":
    main()