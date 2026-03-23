"""Главный модуль e-commerce приложения."""

from src.classes import Product, Category
from src.utils import load_categories_from_json
import json


def main() -> None:
    """Основная функция приложения."""
    # Создание тестовых продуктов
    product1 = Product("Смартфон", "Мощный смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой ноутбук", 80000.0, 5)

    # Создание категории с продуктами
    electronics = Category(
        "Электроника",
        "Различные электронные устройства",
        [product1, product2]
    )

    print(f"Категория: {electronics.name}")
    print(f"Количество категорий: {Category.category_count}")
    print(f"Количество продуктов: {Category.product_count}")

    # Пример загрузки из JSON
    try:
        categories = load_categories_from_json("data/products.json")
        for category in categories:
            print(f"Загружена категория: {category.name}")
            print(f"  Товаров в категории: {len(category.products)}")
    except FileNotFoundError:
        print("Файл products.json не найден")
    except json.JSONDecodeError:
        print("Ошибка при чтении JSON файла")


if __name__ == "__main__":
    main()
