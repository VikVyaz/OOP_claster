from src.abstract import BaseProduct


class Test(BaseProduct):

    @classmethod
    def new_product(cls, product_data):
        super().new_product([])

    def price(self):
        super().price()


test_class = Test


def test_abstract():
    assert test_class.new_product([]) is None
    # assert test_class.price() ???
