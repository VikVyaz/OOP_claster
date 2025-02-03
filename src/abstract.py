from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для Product-подобного"""

    @classmethod
    @abstractmethod
    def new_product(cls, product_data):
        pass

    @property
    @abstractmethod
    def price(self) -> int | float:
        pass


class BaseTradeTurnover(ABC):
    """Абстрактный класс для Product и Order"""

    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def products(self):
        pass
