"""Утилиты для работы с данными."""

import json
from typing import List, Dict, Any
from src.classes import Product, Category


def load_categories_from_json(filepath: str) -> List[Category]:
    """
    Загрузка категорий и товаров из JSON файла.

    Args:
        filepath: Путь к JSON файлу

    Returns:
        Список объектов Category
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        data: List[Dict[str, Any]] = json.load(file)

    categories = []

    for category_data in data:
        products = []

        for product_data in category_data.get('products', []):
            product = Product(
                name=product_data.get('name', ''),
                description=product_data.get('description', ''),
                price=product_data.get('price', 0.0),
                quantity=product_data.get('quantity', 0)
            )
            products.append(product)

        category = Category(
            name=category_data.get('name', ''),
            description=category_data.get('description', ''),
            products=products
        )
        categories.append(category)

    return categories
