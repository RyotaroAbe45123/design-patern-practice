from framework.factory import Factory
from framework.product import Product
from .concrete_product import ConcreteProduct

class ConcreteFactory(Factory):
    def create_product(self, product_name: str) -> Product:
        print(f"create: {product_name}")
        return ConcreteProduct(product_name)

    def register_product(self, product: Product) -> None:
        print(f"register: {product.name}")

    def __private(self):
        print("private function???")
