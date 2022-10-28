from singleton import Singleton


def main() -> None:
    a = Singleton(value=1)
    print(f"a: {a.__value}")

    b = Singleton(value=2)
    print(f"a: {a.__value}")
    print(f"b: {b.__value}")


if __name__ == "__main__":
    main()