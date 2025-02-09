from src.abstract import BaseProduct, BaseTradeTurnover
from src.exceptions import ZeroQuantityError
from src.mixin import MixinPrinting


class Product(BaseProduct, MixinPrinting):
    """
    Класс для предоставления продукта
    """

    name: str
    description: str
    __price: int | float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация Product"""
        if quantity <= 0:
            raise ZeroQuantityError(
                "Товар с нулевым количеством не может быть добавлен"
            )
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Пользовательская информация о продукте"""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> int | float | None:
        """Метод общей стоимости (кол-во * цену) двух продуктов"""

        if type(other) is Product:
            return (self.quantity * self.__price) + (other.quantity * other.__price)
        raise TypeError("Error")

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод создания нового продукта"""

        name, description, price, quantity = product_data.values()
        return cls(name, description, price, quantity)

    @property
    def price(self) -> int | float:
        """Геттер цены продукта"""

        return self.__price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Сеттер цены с проверками на < 0 и < актуальной цены"""

        if new_price <= 0.0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            proof = input(
                "Цена ниже прежней. Установить новую цену: y - да, n - нет:\n"
            )
            if proof == "n":
                print("Изменения отменены")
            else:
                self.__price = new_price
        else:
            self.__price = new_price


class Category(BaseTradeTurnover):
    """
    Класс для предоставления категории
    """

    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Инициализация Category"""

        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        """Информация о продуктах в экземпляре Category"""

        prods_in_cat = 0
        for prod in self.__products:
            prods_in_cat += prod.quantity
        return f"{self.name}, количество продуктов: {prods_in_cat}"

    def __len__(self) -> int:
        """len() для экземпляра Category"""

        return len(self.__products)

    def __getitem__(self, index: int) -> Product:
        """Метод, позволяющий работать с индексами в списке продуктов"""

        return self.__products[index]

    def add_product(self, product) -> None:
        """Метод добавления продукта/ов в категорию"""
        if isinstance(product, Product):
            for prod in self.__products:
                if product.name == prod.name:
                    prod.quantity += product.quantity
                    break
            else:
                self.__products.append(product)
                Category.product_count += 1
        else:
            raise TypeError("Error")

    def for_tests_prods(self) -> list:
        """Технический метод для тестов
        После 'релиза' можно сделать приватным,
        а в тестах прописать ссылку формата (_Category__for_tests_prods)
        """

        return self.__products

    @property
    def products(self):
        """Геттер вывода перечня продуктов в категории"""

        if self.__products:
            return_prods = ""
            for prod in self.__products:
                return_prods += f"{str(prod)}\n"
            return return_prods
        return "Список продуктов пуст"

    @property
    def average_price(self):
        try:
            return sum(prod.price for prod in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0


class Order(BaseTradeTurnover):
    """
    Класс для предоставления заказа
    """

    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity
        self.order_cost = product.price * quantity

    def add_product(self, product):
        pass

    def products(self):
        pass


class CatIter:
    """Итератор по продуктам для Category"""

    category: Category

    def __init__(self, category: Category):
        """Инициализация итератора"""

        self.cat = category

    def __iter__(self):
        """Итератор"""

        self.index = -1
        return self

    def __next__(self):
        """next() итератора"""

        if self.index < len(self.cat) - 1:
            self.index += 1
            return self.cat[self.index]
        else:
            raise StopIteration
