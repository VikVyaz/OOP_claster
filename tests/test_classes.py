from unittest.mock import patch

from src.classes import Category, Product


def test_product_init(prod_init_list: list) -> None:
    """Тест инициализации Product"""

    for prod in prod_init_list:
        assert prod.name in [
            "Samsung Galaxy S23 Ultra",
            "Iphone 15",
            "Xiaomi Redmi Note 11",
        ]
        assert prod.description in [
            "256GB, Серый цвет, 200MP камера",
            "512GB, Gray space",
            "1024GB, Синий",
        ]
        assert prod.price in [180000.0, 210000.0, 31000.0]
        assert prod.quantity in [5, 8, 14]


def test_category_counters_1(cat_init_list) -> None:
    """Тест счетчика категорий и продуктов в них"""

    test_cat = cat_init_list[0]
    assert test_cat.category_count == 2
    assert test_cat.product_count == 6


def test_category_init(cat_init_list: list, prod_init_list) -> None:
    """Тест инициализации Category"""

    for cat in cat_init_list:
        assert cat.name in ["Смартфоны", "Телевизоры"]
        assert cat.description in ["Описание1", "Описание2"]
        for prod in cat.for_tests_prods():
            assert isinstance(prod, type(prod_init_list[0]))


def test_clsmethod_product():
    """Тест класс-метода Product.new_product()"""

    test_prod = Product.new_product(
        {"name": "1", "description": "2", "price": 3, "quantity": 4}
    )
    assert test_prod.name == "1"
    assert test_prod.description == "2"
    assert test_prod.price == 3
    assert test_prod.quantity == 4


def test_prod_getter_price(prod_init_list):
    """Тест геттера цены в Product"""

    assert prod_init_list[1].price == 210000.0


@patch("src.classes.input")
def test_prod_setter_price(mock_input, prod_init_list, capsys):
    """Тест сеттера цены в Product"""

    test_prod = prod_init_list[0]
    test_prod.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    test_prod.price = 10
    mock_input.return_value = "y"
    assert test_prod.price == 10

    mock_input.return_value = "n"
    test_prod.price = 5
    message = capsys.readouterr()
    assert message.out.strip() == "Изменения отменены"
    assert test_prod.price == 10

    test_prod.price = 200000
    assert test_prod.price == 200000


def test_add_prod_in_category(fixt_add_prod):
    """Тест добавления продукта в категорию в Category"""

    fixt_add_prod["cat"].add_product(fixt_add_prod["prod_to_add_1"])
    assert (
        fixt_add_prod["cat"].for_tests_prods()[0].quantity
        == fixt_add_prod["prod_to_add_1"].quantity * 2
    )
    fixt_add_prod["cat"].add_product(fixt_add_prod["prod_to_add_2"])
    assert len(fixt_add_prod["cat"].for_tests_prods()) == 2


def test_products_print_in_category(fixt_add_prod):
    """Тест геттера products в Category"""

    assert fixt_add_prod["cat"].products == "test_prod, 1.0 руб. Остаток: 1 шт.\n"
    test_empty = Category("test", "test")
    assert test_empty.products == "Список продуктов пуст"
