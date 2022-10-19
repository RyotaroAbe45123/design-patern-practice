from framework.product import Product

class ConcreteProduct(Product):
    def __init__(self, product_name: str) -> None:
        self.name = product_name

    def cut(self):
        print(f"--cut: {self.name}--")

    def draw(self):
        print(f"++draw: {self.name}++")
