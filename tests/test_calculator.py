"""
Unit-тесты для параметрических функций калькулятора
Используется pytest для тестирования
"""

import pytest
import sys
import os

# Добавляем родительскую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import (
    addition, subtraction, multiplication, 
    division, exponentiation, square_root
)


class TestCalculator:
    """Тестовый класс для функций калькулятора"""
    
    def test_addition_positive(self):
        """Тест сложения положительных чисел"""
        assert addition(5, 3) == 8
        assert addition(10.5, 2.5) == 13.0
        assert addition(0, 0) == 0
    
    def test_addition_negative(self):
        """Тест сложения отрицательных чисел"""
        assert addition(-5, -3) == -8
        assert addition(-10, 5) == -5
    
    def test_subtraction_positive(self):
        """Тест вычитания положительных чисел"""
        assert subtraction(10, 3) == 7
        assert subtraction(5.5, 2.5) == 3.0
    
    def test_subtraction_negative(self):
        """Тест вычитания отрицательных чисел"""
        assert subtraction(5, 10) == -5
        assert subtraction(-5, -3) == -2
    
    def test_multiplication_positive(self):
        """Тест умножения положительных чисел"""
        assert multiplication(4, 3) == 12
        assert multiplication(2.5, 4) == 10.0
    
    def test_multiplication_negative(self):
        """Тест умножения отрицательных чисел"""
        assert multiplication(-4, 3) == -12
        assert multiplication(-2, -5) == 10
        assert multiplication(0, 5) == 0
    
    def test_division_positive(self):
        """Тест деления положительных чисел"""
        assert division(10, 2) == 5
        assert division(5, 2) == 2.5
        assert division(0, 5) == 0
    
    def test_division_negative(self):
        """Тест деления отрицательных чисел"""
        assert division(-10, 2) == -5
        assert division(10, -2) == -5
    
    def test_division_by_zero(self):
        """Тест деления на ноль (должен вызывать исключение)"""
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            division(10, 0)
    
    def test_exponentiation_positive(self):
        """Тест возведения в степень положительных чисел"""
        assert exponentiation(2, 3) == 8
        assert exponentiation(5, 2) == 25
        assert exponentiation(4, 0.5) == 2
    
    def test_exponentiation_negative(self):
        """Тест возведения в степень отрицательных чисел"""
        assert exponentiation(2, -1) == 0.5
        assert exponentiation(-2, 3) == -8
        assert exponentiation(-2, 2) == 4
    
    def test_square_root_positive(self):
        """Тест извлечения квадратного корня положительных чисел"""
        assert square_root(25) == 5
        assert square_root(0) == 0
        assert square_root(2.25) == 1.5
    
    def test_square_root_negative(self):
        """Тест извлечения корня из отрицательного числа (должен вызывать исключение)"""
        with pytest.raises(ValueError, match="Квадратный корень из отрицательного числа не определен"):
            square_root(-9)
    
    def test_edge_cases(self):
        """Тест граничных случаев"""
        # Большие числа
        assert addition(1e6, 1e6) == 2e6
        # Очень маленькие числа
        assert multiplication(0.0001, 0.0001) == 1e-8
        # Степень 0
        assert exponentiation(100, 0) == 1


if __name__ == "__main__":
    # Запуск тестов через pytest
    pytest.main([__file__, "-v"])