from concrete.concrete_factory import ConcreteFactory


def main():
    factory = ConcreteFactory()
    hoge = factory.create("hoge")
    hoge.print()
    fuga = factory.create("fuga")
    fuga.print()
    # print(dir(factory))
    # factory.__private()
    # factory._Factory__private()

if __name__ == "__main__":
    main()