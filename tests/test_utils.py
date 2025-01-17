from unittest.mock import patch, mock_open, MagicMock
from src.utils import to_open_file, to_create_category_object
from src.classes import Product, Category


@patch("builtins.open", new_callable=mock_open)
@patch('json.load')
def test_open_file(mock_load, mock_open_file: MagicMock):

    mock_load.return_value = '123'
    assert to_open_file('123') == '123'


@patch('src.utils.to_open_file')
def test_to_create_category_object(mock_open_file, fixt_cat_create, prod_init_list):
    mock_open_file.return_value = fixt_cat_create
    result = to_create_category_object('123')[0]
    assert isinstance(result, Category)
    assert isinstance(result.for_tests_prods()[0], Product)
