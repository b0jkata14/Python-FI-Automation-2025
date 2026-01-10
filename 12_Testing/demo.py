"""
1) unittest (вграден в Python)
   - подробно (-v, verbose):
     python -m unittest -v demo.py

   - само един тестов клас:
     python -m unittest demo.TestDivideUnittest

2) pytest (външна библиотека)
   - инсталация:
     pip install pytest

   - стартиране:
     pytest -v demo.py

ЗАБЕЛЕЖКА:
В реални проекти тестовете и бизнес логиката са в отделни файлове.
Тестовите файлове се именуват с префикс `test_` (напр. `test_fizzbuzz.py`).
"""


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers!")

    return a / b


def valid_age(age):
    """
    Проверка дали потребителят е пълнолетен.
    """
    # ^ Това е docstring и се достъпва: valid_age.__doc__

    if not isinstance(age, int):
        raise TypeError("Age must be whole number!")

    return age >= 18


def calculate_price(price, discount):
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("price and discount must be numbers!")

    if price < 0:
        raise ValueError("Price can't be negative!")

    if not (0 <= discount <= 1):
        raise ValueError("Discount must be in the range 0 - 1")

    return price - price * discount


def checkout(price):
    """
    Пример за интеграционен тест:
    checkout използва calculate_price вътрешно.
    """
    return calculate_price(price, 0.1)


def fizzbuzz(n):
    """
    Класически FizzBuzz пример (подходящ за TDD - Test-Driven Development).
    """
    if not isinstance(n, int):
        raise TypeError("n must be whole number!")

    if n <= 0:
        raise ValueError("n must be positive!")

    if n % 15 == 0:
        return "Fizz Buzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"

    return str(n)


# =====================================================
# UNITTEST — класическият (стандартен) подход
#
# ПРИНЦИП FIRST за качествени unit тестове:
# F - Fast (бързи) → да се пускат често
# I - Independent (независими) → тестовете да не зависят един от друг
# R - Repeatable (повторяеми) → винаги да дават един и същ резултат
# S - Self-validating (самовалидиращи) → PASS/FAIL автоматично, без "гледане на око"
# T - Timely (навременни) → пишат се рано (често преди/по време на кода, TDD)
# =====================================================

import unittest


class TestDivideUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Изпълнява се ВЕДНЪЖ преди всички тестове в класа.
        Подходящо за тежки ресурси (DB, конфигурации и т.н.)
        """
        cls.shared_data = (10, 2)

    @classmethod
    def tearDownClass(cls):
        """
        Изпълнява се ВЕДНЪЖ след всички тестове в класа.
        """
        cls.shared_data = None

    def setUp(self):
        """
        Изпълнява се ПРЕДИ всеки тест.
        """
        self.a, self.b = self.shared_data

    def tearDown(self):
        """
        Изпълнява се СЛЕД всеки тест.
        """
        self.a = None
        self.b = None

    def test_divide_happy_path(self):
        """Проверка на нормален (happy path) сценарий"""
        self.assertEqual(divide(self.a, self.b), 5)

    def test_divide_by_zero(self):
        """Проверка за очаквано изключение"""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_invalid_types(self):
        """Тестваме няколко грешни входа с subTest"""
        cases = [
            ("10", 2),
            (10, "2"),
            (None, 2),
        ]

        for a, b in cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(TypeError):
                    divide(a, b)

    @unittest.skip("Пример за skip – тестът е изключен нарочно")
    def test_skip_example(self):
        self.assertEqual(divide(8, 2), 4)

    @unittest.skipIf(True, "Пример за skipIf – зависи от условие")
    def test_skipif_example(self):
        self.assertEqual(divide(9, 3), 3)


class TestBusinessLogicUnittest(unittest.TestCase):
    def test_valid_age(self):
        self.assertTrue(valid_age(18))
        self.assertFalse(valid_age(17))

    def test_valid_age_wrong_type(self):
        with self.assertRaises(TypeError):
            valid_age("18")

    def test_calculate_price(self):
        self.assertEqual(calculate_price(100, 0.1), 90)

    def test_checkout_integration(self):
        """
        Интеграционен тест:
        не ни интересува как е имплементирана отстъпката,
        а дали checkout връща правилния резултат.
        """
        self.assertEqual(checkout(100), 90)

    @unittest.expectedFailure
    def test_known_bug_demo(self):
        """
        expectedFailure:
        тестът се проваля, но това е ОЧАКВАНО.
        Полезно при известен бъг.
        """
        self.assertEqual(checkout(100), 95)


class TestFizzBuzzUnittest(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")

    def test_rules(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(15), "Fizz Buzz")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fizzbuzz(0)
        with self.assertRaises(TypeError):
            fizzbuzz("15")


# =====================================================
# PYTEST — модерен, функционален стил
# =====================================================
# Ако pytest не е инсталиран, тази секция се пропуска и файлът си работи с unittest.

try:
    import pytest  # трябва да се инсталира 'pip install pytest'
except ImportError:
    pytest = None

if pytest:

    @pytest.fixture
    def numbers():
        """
        Fixture = pytest еквивалент на setUp.
        """
        return 10, 2

    def test_divide_pytest(numbers):
        a, b = numbers
        assert divide(a, b) == 5

    def test_divide_raises_pytest():
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, "1"),
            (3, "Fizz"),
            (5, "Buzz"),
            (15, "Fizz Buzz"),
        ]
    )
    def test_fizzbuzz_parametrized(n, expected):
        assert fizzbuzz(n) == expected

    @pytest.mark.skip(reason="Пример за skip в pytest")
    def test_skip_pytest():
        assert checkout(100) == 90

    @pytest.mark.xfail(reason="Очаквано проваляне (xfail)")
    def test_xfail_pytest():
        assert checkout(100) == 95


# =====================================================
# РЪЧНО СТАРТИРАНЕ (НЕ Е ТЕСТ)
# =====================================================

if __name__ == "__main__":
    print("Бърза ръчна проверка (НЕ тестове):")
    print("divide(10, 2) =", divide(10, 2))

    try:
        divide(10, 0)
    except Exception as e:
        print("divide(10, 0) хвърли:", repr(e))

# ПОКРИТИЕ (Coverage):
# 1) инсталация:
#   pip install coverage
#
# 2) покритие с unittest:
#   coverage run -m unittest -v demo.py
#   coverage report -m
#
# 3) покритие с pytest:
#   pip install pytest-cov
#   pytest -v --cov demo.py
