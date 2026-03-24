"""Тесты для утилит загрузки данных."""

import json
import pytest
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
            assert category.description == "Описание тестовой категории"
            # Проверяем, что products возвращает строку с продуктом
            assert "Тестовый продукт" in category.products
            assert "1000.5" in category.products
            assert "Остаток: 10" in category.products

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
            assert "Продукт 1" in categories[0].products
            assert "Продукт 2" in categories[1].products

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
            assert categories[0].products == ""  # пустая строка для пустой категории

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
            assert category.description == ""  # значение по умолчанию

            # Проверяем, что продукт создался с значениями по умолчанию
            assert "Продукт без цены" in category.products
            assert "0.0" in category.products  # цена по умолчанию
            assert "Остаток: 5" in category.products

    def test_load_file_not_found(self):
        """Тест обработки отсутствующего файла."""
        with pytest.raises(FileNotFoundError):
            load_categories_from_json("non_existent_file.json")

    def test_load_invalid_json(self):
        """Тест обработки некорректного JSON."""
        mock_data = "this is not valid json"

        with patch("builtins.open", mock_open(read_data=mock_data)):
            with pytest.raises(json.JSONDecodeError):
                load_categories_from_json("dummy_path.json")
