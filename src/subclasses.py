from src.classes import Product


class Smartphone(Product):
    """Subclass Product для смартфонов"""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other) -> int | float | None:
        """Метод сложения исключительно Smartphone объектов"""

        if type(other) is Smartphone:
            return (self.quantity * self.price) + (other.quantity * other.price)
        raise TypeError("Error")


class LawnGrass(Product):
    """Subclass Product для газонной травы"""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other) -> int | float | None:
        """Метод сложения исключительно LawnGrass объектов"""

        if type(other) is LawnGrass:
            return (self.quantity * self.price) + (other.quantity * other.price)
        raise TypeError("Error")
