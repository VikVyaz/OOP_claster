class Product:
    """
    Класс для предоставления продукта
    """

    name: str
    description: str
    __price: int | float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация Product"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Пользовательская информация о продукте"""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> int | float | None:
        """Метод общей стоимости (кол-во * цену) двух продуктов"""

        if isinstance(other, Product):
            return (self.quantity * self.__price) + (other.quantity * other.__price)
        else:
            return None

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


class Category:
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

    def add_product(self, product: Product) -> None:
        """Метод добавления продукта/ов в категорию"""

        for prod in self.__products:
            if product.name == prod.name:
                prod.quantity += product.quantity
                break
        else:
            self.__products.append(product)
            Category.product_count += 1

    def for_tests_prods(self) -> list:
        """Технический метод для тестов
        После 'релиза' можно сделать приватным,
        а в тестах прописать ссылку формата (_Category__for_tests_prods)
        """

        return self.__products

    @property
    def products(self) -> str:
        """Геттер вывода перечня продуктов в категории"""

        if self.__products:
            return_prods = ""
            for prod in self.__products:
                return_prods += str(prod)
            return return_prods
        return "Список продуктов пуст"


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
