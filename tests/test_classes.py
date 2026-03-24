"""Тесты для классов Product и Category."""

import pytest
from src.classes import Product, Category


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self):
        """Тест корректной инициализации продукта."""
        product = Product("Телефон", "Смартфон", 30000.0, 15)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 30000.0
        assert product.quantity == 15

    def test_product_with_float_price(self):
        """Тест продукта с ценой с копейками."""
        product = Product("Наушники", "Беспроводные", 2999.99, 50)

        assert product.price == 2999.99
        assert isinstance(product.price, float)

    def test_product_zero_quantity(self):
        """Тест продукта с нулевым количеством."""
        product = Product("Чехол", "Силиконовый", 500.0, 0)

        assert product.quantity == 0

    def test_price_setter_positive(self):
        """Тест сеттера цены с положительным значением."""
        product = Product("Телефон", "Смартфон", 30000.0, 15)
        product.price = 35000.0

        assert product.price == 35000.0

    def test_price_setter_negative(self, capsys):
        """Тест сеттера цены с отрицательным значением."""
        product = Product("Телефон", "Смартфон", 30000.0, 15)
        product.price = -1000.0

        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 30000.0  # цена не изменилась

    def test_price_setter_zero(self, capsys):
        """Тест сеттера цены с нулевым значением."""
        product = Product("Телефон", "Смартфон", 30000.0, 15)
        product.price = 0

        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 30000.0  # цена не изменилась

    def test_new_product_classmethod(self):
        """Тест класс-метода new_product."""
        product_data = {
            'name': 'Ноутбук',
            'description': 'Мощный ноутбук',
            'price': 75000.0,
            'quantity': 10
        }

        product = Product.new_product(product_data)

        assert product.name == 'Ноутбук'
        assert product.description == 'Мощный ноутбук'
        assert product.price == 75000.0
        assert product.quantity == 10


class TestCategory:
    """Тесты для класса Category."""

    @pytest.fixture(autouse=True)
    def reset_class_attributes(self):
        """Сброс атрибутов класса перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0
        yield

    def test_category_initialization(self):
        """Тест корректной инициализации категории."""
        products = [
            Product("Товар1", "Описание1", 100.0, 10),
            Product("Товар2", "Описание2", 200.0, 20)
        ]
        category = Category("Категория1", "Описание категории", products)

        assert category.name == "Категория1"
        assert category.description == "Описание категории"

    def test_category_count_increments(self):
        """Тест подсчета количества категорий."""
        Category("Кат1", "Описание1", [])
        Category("Кат2", "Описание2", [])
        Category("Кат3", "Описание3", [])

        assert Category.category_count == 3

    def test_product_count_increments(self):
        """Тест подсчета количества продуктов."""
        products1 = [
            Product("Товар1", "Описание1", 100.0, 10),
            Product("Товар2", "Описание2", 200.0, 20)
        ]
        Category("Кат1", "Описание1", products1)
        assert Category.product_count == 2

        products2 = [Product("Товар3", "Описание3", 300.0, 30)]
        Category("Кат2", "Описание2", products2)
        assert Category.product_count == 3

    def test_empty_category(self):
        """Тест категории без продуктов."""
        Category("Пустая", "Нет товаров", [])

        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_add_product(self):
        """Тест добавления продукта через метод add_product."""
        category = Category("Электроника", "Различные устройства", [])
        product = Product("Смартфон", "Мощный смартфон", 50000.0, 10)

        category.add_product(product)

        # Проверяем, что продукт добавился через геттер
        products_str = category.products
        assert "Смартфон" in products_str
        assert "50000.0" in products_str
        assert "Остаток: 10" in products_str
        assert Category.product_count == 1

    def test_add_multiple_products(self):
        """Тест добавления нескольких продуктов."""
        category = Category("Электроника", "Различные устройства", [])
        product1 = Product("Смартфон", "Мощный смартфон", 50000.0, 10)
        product2 = Product("Ноутбук", "Игровой ноутбук", 80000.0, 5)

        category.add_product(product1)
        category.add_product(product2)

        products_str = category.products
        assert "Смартфон" in products_str
        assert "Ноутбук" in products_str
        assert Category.product_count == 2

    def test_products_getter_format(self):
        """Тест формата вывода геттера products."""
        category = Category("Электроника", "Различные устройства", [])
        product = Product("Смартфон", "Мощный смартфон", 50000.0, 10)

        category.add_product(product)

        expected = "Смартфон, 50000.0 руб. Остаток: 10 шт.\n"
        assert category.products == expected

    def test_products_getter_empty(self):
        """Тест геттера products для пустой категории."""
        category = Category("Пустая", "Нет товаров", [])
        assert category.products == ""

    def test_products_private_attribute(self):
        """Тест, что атрибут products приватный."""
        category = Category("Электроника", "Различные устройства", [])

        with pytest.raises(AttributeError):
            _ = category.__products
