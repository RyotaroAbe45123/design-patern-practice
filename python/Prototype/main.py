from teacher import Teacher
from prototype.paper import Paper
from prototype.book import Book


def main():
    teacher = Teacher()

    paper = Paper("paper")

    teacher.register("paper", paper)

    papers = teacher.create_many_crystals("paper")
    print(len(papers))
    print(papers[0])
    print(papers[1])
    print(papers[2])


    book = Book()

    teacher.register("book", book)

    books = teacher.create_many_crystals("book")
    print(len(books))
    print(books[0])
    print(books[1])
    print(books[2])


if __name__ == "__main__":
    main()