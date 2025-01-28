import pytest


# ---------------------------------------------------class Smartphone(Product)-----------------------------------------
def test_smartphone_init(fix_smartphone):
    """Тест инициализации Smartphone"""

    assert fix_smartphone[0].name == "test_name"
    assert fix_smartphone[0].description == "test_discr"
    assert fix_smartphone[0].price == 1
    assert fix_smartphone[0].quantity == 1
    assert fix_smartphone[0].efficiency == "test"
    assert fix_smartphone[0].model == "test_model"
    assert fix_smartphone[0].memory == 1
    assert fix_smartphone[0].color == "test_color"


def test_smartphone_add(fix_smartphone):
    assert fix_smartphone[0] + fix_smartphone[1] == 2
    with pytest.raises(TypeError):
        error = fix_smartphone[0] + 1


# ----------------------------------------------------class LawnGrass(Product)-----------------------------------------
def test_lawngrass_init(fix_lawngrass):
    """Тест инициализации lawngrass"""

    assert fix_lawngrass[0].name == "test"
    assert fix_lawngrass[0].description == "test"
    assert fix_lawngrass[0].price == 1
    assert fix_lawngrass[0].quantity == 1
    assert fix_lawngrass[0].country == "test"
    assert fix_lawngrass[0].germination_period == "test"
    assert fix_lawngrass[0].color == "test"


def test_lawngrass_add(fix_lawngrass):
    assert fix_lawngrass[0] + fix_lawngrass[1] == 2
    with pytest.raises(TypeError):
        error = fix_lawngrass[0] + 1
