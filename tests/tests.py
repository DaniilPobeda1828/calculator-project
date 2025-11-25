import pytest
from сalculator import division


def test_division_by_zero(self):
    """Тест деления на ноль (должен вызывать исключение)"""
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        division(10, 0)