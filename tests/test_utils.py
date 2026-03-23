"""Тесты для утилит загрузки данных."""

import json
from unittest.mock import mock_open, patch
from src.utils import load_categories_from_json


class TestLoadCategoriesFromJson:
    """Тесты для функции загрузки категорий из JSON."""

    def test_load_categories_success(self):
        """Тест успешной загрузки категорий из JSON."""
        test_data = [
            {
                "name": "Тестовая категория",
                "description": "Описание тестовой категории",
                "products": [
                    {
                        "name": "Тестовый продукт",
                        "description": "Описание тестового продукта",
                        "price": 1000.50,
                        "quantity": 10,
                    }
                ],
            }
        ]

        mock_data = json.dumps(test_data, ensure_ascii=False)

        with patch("builtins.open", mock_open(read_data=mock_data)):
            categories = load_categories_from_json("dummy_path.json")

            assert len(categories) == 1
            category = categories[0]
            assert category.name == "Тестовая категория"
            assert len(category.products) == 1

    def test_load_multiple_categories(self):
        """Тест загрузки нескольких категорий."""
        test_data = [
            {
                "name": "Категория 1",
                "description": "Описание 1",
                "products": [
                    {
                        "name": "Продукт 1",
                        "description": "Описание продукта 1",
                        "price": 100.0,
                        "quantity": 5,
                    }
                ],
            },
            {
                "name": "Категория 2",
                "description": "Описание 2",
                "products": [
                    {
                        "name": "Продукт 2",
                        "description": "Описание продукта 2",
                        "price": 200.0,
                        "quantity": 10,
                    }
                ],
            },
        ]

        mock_data = json.dumps(test_data, ensure_ascii=False)

        with patch("builtins.open", mock_open(read_data=mock_data)):
            categories = load_categories_from_json("dummy_path.json")

            assert len(categories) == 2
            assert categories[0].name == "Категория 1"
            assert categories[1].name == "Категория 2"

    def test_load_empty_products(self):
        """Тест загрузки категории без продуктов."""
        test_data = [
            {
                "name": "Пустая категория",
                "description": "Категория без товаров",
                "products": [],
            }
        ]

        mock_data = json.dumps(test_data, ensure_ascii=False)

        with patch("builtins.open", mock_open(read_data=mock_data)):
            categories = load_categories_from_json("dummy_path.json")

            assert len(categories) == 1
            assert len(categories[0].products) == 0

    def test_load_missing_fields(self):
        """Тест загрузки данных с отсутствующими полями."""
        test_data = [
            {
                "name": "Категория без описания",
                "products": [
                    {"name": "Продукт без цены", "quantity": 5}
                ],
            }
        ]

        mock_data = json.dumps(test_data, ensure_ascii=False)

        with patch("builtins.open", mock_open(read_data=mock_data)):
            categories = load_categories_from_json("dummy_path.json")

            category = categories[0]
            assert category.description == ""

            product = category.products[0]
            assert product.description == ""
            assert product.price == 0.0
