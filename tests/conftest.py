from typing import Generator

import pytest

from src.classes import Category, Product


@pytest.fixture()
def prod_init_list() -> list:
    return [
        Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        ),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture()
def cat_init_list(prod_init_list) -> Generator:
    amount = Category.category_count
    yield [
        Category("Смартфоны", "Описание1", prod_init_list),
        Category("Телевизоры", "Описание2", prod_init_list),
    ]
    Category.category_count = amount


@pytest.fixture()
def fixt_cat_create():
    return [{
        "name": "",
        "description": "",
        "products": [{
            "name": "123",
            "description": "123",
            "price": 0.0,
            "quantity": 0
        }]
    }]
