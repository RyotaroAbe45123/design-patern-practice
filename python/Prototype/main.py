from teacher import Teacher
from prototype.paper import Paper


def main():
    teacher = Teacher()

    paper = Paper("paper")

    teacher.register("paper", paper)

    papers = teacher.create_many_crystals("paper")
    print(papers[0])
    print(papers[1])


if __name__ == "__main__":
    main()