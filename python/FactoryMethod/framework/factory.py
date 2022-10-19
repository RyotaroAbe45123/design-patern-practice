from abc import ABC, abstractmethod

from .product import Product


class Factory(ABC):
    def create(self):
        product = self.create_product()
        self.register_product(product)

    @abstractmethod
    def create_product(self) -> Product:
        pass

    @abstractmethod
    def register_product(self) -> None:
        pass
