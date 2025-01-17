import json
from typing import Any

from src.classes import Category, Product


def to_open_file(path: str) -> Any:
    """
    Функция открытия JSON-файла
    """

    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        return data


def to_create_category_object(path: str) -> list:
    """
    Функция создания класса Category из JSON-файла
    """

    result = []
    data = to_open_file(path)
    for cat in data:
        result_category = []
        for prod in cat["products"]:
            result_category.append(Product(**prod))
        cat["products"] = result_category
        result.append(Category(**cat))

    return result


# if __name__ == '__main__':
#     res = to_create_category_object('../data/products.json')
#     print(f'Результат utils.py, создание объектов класса Category:\n{res}')
#     print(f'Объекты Product в объектах Category.product:\n{res[0].products}')
