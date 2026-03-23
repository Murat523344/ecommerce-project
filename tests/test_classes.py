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
        assert len(category.products) == 2
        assert category.products[0].name == "Товар1"
        assert category.products[1].name == "Товар2"

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

    def test_category_with_multiple_products(self):
        """Тест категории с несколькими продуктами."""
        products = [
            Product("П1", "О1", 100.0, 5),
            Product("П2", "О2", 200.0, 10),
            Product("П3", "О3", 300.0, 15),
            Product("П4", "О4", 400.0, 20)
        ]
        Category("Большая", "Много товаров", products)

        assert Category.product_count == 4
