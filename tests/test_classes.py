from src.classes import Category


def test_product_init(prod_init_list: list) -> None:
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
    test_cat = cat_init_list[0]
    assert test_cat.category_count == 2
    assert test_cat.product_count == 6


def test_category_init(cat_init_list: list, prod_init_list) -> None:
    for cat in cat_init_list:
        assert cat.name in ["Смартфоны", "Телевизоры"]
        assert cat.description in ["Описание1", "Описание2"]
        for prod in cat.products:
            assert isinstance(prod, type(prod_init_list[0]))
