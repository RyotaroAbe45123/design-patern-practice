from singleton import Singleton


def main() -> None:
    a = Singleton()
    print(a)
    b = Singleton()
    print(b)

    return None
    a = Singleton(value=1)
    try:
        print(f"a, _value: {a._value}")
        print(f"a, __value: {a.__value}")
    except AttributeError as e:
        print(f"a, dir: {dir(a)}")

    b = Singleton(value=2)
    try:
        print(f"a, _value: {a._value}")
        print(f"a, __value: {a.__value}")
        print(f"b, _value: {b._value}")
        print(f"b, __value: {b.__value}")
    except AttributeError as e:
        print(f"a, dir: {dir(a)}")
        print(f"b, dir: {dir(b)}")

if __name__ == "__main__":
    main()