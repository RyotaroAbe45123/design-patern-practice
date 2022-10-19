from framework.factory import Factory
from framework.product import Product
from concrete.concrete_factory import ConcreteFactory


def main():
    factory: Factory = ConcreteFactory()
    hoge: Product = factory.create("hoge")
    hoge.print()
    fuga: Product = factory.create("fuga")
    fuga.print()
    # print(dir(factory))
    # factory.__private()
    # factory._Factory__private()

if __name__ == "__main__":
    main()