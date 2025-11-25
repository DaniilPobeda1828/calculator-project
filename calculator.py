"""
Программа-калькулятор с базовыми математическими операциями
Поддерживает: сложение, вычитание, умножение, деление, возведение в степень, извлечение корня

Версия: 2.0
Изменения: все расчетные функции переписаны в параметрическом виде
"""

import math


def show_menu():
    """
    Функция для отображения меню доступных операций
    """
    print("\n" + "="*50)
    print("      КАЛЬКУЛЯТОР (Параметрическая версия)")
    print("="*50)
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Квадратный корень (√)")
    print("7. Выход")
    print("="*50)


def get_number(prompt):
    """
    Функция для безопасного ввода числа с обработкой ошибок
    
    Args:
        prompt (str): Подсказка для пользователя
    
    Returns:
        float: Введенное пользователем число
    """
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")


def addition(a, b):
    """
    Параметрическая функция для выполнения операции сложения
    
    Args:
        a (float): Первое слагаемое
        b (float): Второе слагаемое
    
    Returns:
        float: Результат сложения a + b
    """
    return a + b


def subtraction(a, b):
    """
    Параметрическая функция для выполнения операции вычитания
    
    Args:
        a (float): Уменьшаемое
        b (float): Вычитаемое
    
    Returns:
        float: Результат вычитания a - b
    """
    return a - b


def multiplication(a, b):
    """
    Параметрическая функция для выполнения операции умножения
    
    Args:
        a (float): Первый множитель
        b (float): Второй множитель
    
    Returns:
        float: Результат умножения a * b
    """
    return a * b


def division(a, b):
    """
    Параметрическая функция для выполнения операции деления
    
    Args:
        a (float): Делимое
        b (float): Делитель
    
    Returns:
        float: Результат деления a / b
    
    Raises:
        ValueError: Если делитель равен нулю
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


def exponentiation(base, exponent):
    """
    Параметрическая функция для выполнения операции возведения в степень
    
    Args:
        base (float): Основание степени
        exponent (float): Показатель степени
    
    Returns:
        float: Результат возведения в степень base ^ exponent
    """
    return base ** exponent


def square_root(number):
    """
    Параметрическая функция для извлечения квадратного корня
    
    Args:
        number (float): Число для извлечения корня
    
    Returns:
        float: Квадратный корень из числа
    
    Raises:
        ValueError: Если число отрицательное
    """
    if number < 0:
        raise ValueError("Квадратный корень из отрицательного числа не определен")
    return math.sqrt(number)


def execute_addition():
    """Функция-обертка для выполнения сложения через UI"""
    print("\n--- СЛОЖЕНИЕ ---")
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    result = addition(num1, num2)
    print(f"Результат: {num1} + {num2} = {result}")


def execute_subtraction():
    """Функция-обертка для выполнения вычитания через UI"""
    print("\n--- ВЫЧИТАНИЕ ---")
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    result = subtraction(num1, num2)
    print(f"Результат: {num1} - {num2} = {result}")


def execute_multiplication():
    """Функция-обертка для выполнения умножения через UI"""
    print("\n--- УМНОЖЕНИЕ ---")
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    result = multiplication(num1, num2)
    print(f"Результат: {num1} × {num2} = {result}")


def execute_division():
    """Функция-обертка для выполнения деления через UI"""
    print("\n--- ДЕЛЕНИЕ ---")
    num1 = get_number("Введите делимое: ")
    
    while True:
        num2 = get_number("Введите делитель: ")
        try:
            result = division(num1, num2)
            print(f"Результат: {num1} ÷ {num2} = {result}")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")


def execute_exponentiation():
    """Функция-обертка для выполнения возведения в степень через UI"""
    print("\n--- ВОЗВЕДЕНИЕ В СТЕПЕНЬ ---")
    base = get_number("Введите основание: ")
    exponent = get_number("Введите степень: ")
    result = exponentiation(base, exponent)
    print(f"Результат: {base} ^ {exponent} = {result}")


def execute_square_root():
    """Функция-обертка для выполнения извлечения корня через UI"""
    print("\n--- КВАДРАТНЫЙ КОРЕНЬ ---")
    
    while True:
        number = get_number("Введите число: ")
        try:
            result = square_root(number)
            print(f"Результат: √{number} = {result}")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")


def main():
    """
    Основная функция программы, содержащая главный цикл калькулятора
    """
    print("Добро пожаловать в калькулятор (Параметрическая версия)!")
    
    while True:
        show_menu()
        choice = input("Выберите операцию (1-7): ")
        
        if choice == '1':
            execute_addition()
        elif choice == '2':
            execute_subtraction()
        elif choice == '3':
            execute_multiplication()
        elif choice == '4':
            execute_division()
        elif choice == '5':
            execute_exponentiation()
        elif choice == '6':
            execute_square_root()
        elif choice == '7':
            print("Спасибо за использование калькулятора! До свидания!")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите операцию от 1 до 7.")
        
        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
