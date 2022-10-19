from abc import ABC, abstractmethod

from .product import Product


class Factory(ABC):
    def create(self, product_name: str):
        product = self.create_product(product_name)
        self.register_product(product)

    @abstractmethod
    def create_product(self, product_name: str) -> Product:
        pass

    @abstractmethod
    def register_product(self, product: Product) -> None:
        pass

    def __private(self):
        print("private function.")
