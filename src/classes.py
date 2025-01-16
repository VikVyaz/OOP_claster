class Product:
    """
    Класс для предоставления продукта
    """

    name: str
    description: str
    price: int | float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        name, description, price, quantity = product_data.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int | float):
        if new_price <= 0.0:
            print('Цена не должна быть нулевая или отрицательная')
        elif new_price < self.__price:
            proof = input('Цена ниже прежней. Установить новую цену: y - да, n - нет:\n')
            if proof == 'n':
                print('Изменения отменены')
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
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product):
        for prod in self.__products:
            if product.name == prod.name:
                prod.quantity += product.quantity
                break
        else:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        if self.__products:
            return_prods = ''
            for prod in self.__products:
                return_prods += f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт. \n'
            return return_prods
        return 'Список продуктов пуст'

