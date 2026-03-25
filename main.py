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
    electronics = Category("Электроника", "Различные электронные устройства", [])

    # Добавление продуктов через метод add_product
    electronics.add_product(product1)
    electronics.add_product(product2)

    print(f"Категория: {electronics.name}")
    print(f"Количество категорий: {Category.category_count}")
    print(f"Количество продуктов: {Category.product_count}")

    # Вывод продуктов через геттер
    print("\nТовары в категории:")
    print(electronics.products)

    # Тестирование строкового представления
    print("\n--- Тестирование __str__ ---")
    print(f"Продукт: {product1}")
    print(f"Категория: {electronics}")

    # Тестирование сложения продуктов
    print("\n--- Тестирование __add__ ---")
    product3 = Product("Планшет", "Удобный планшет", 35000.0, 8)
    total_cost = product1 + product3
    print(f"Стоимость товаров на складе: {total_cost} руб.")
    print(
        f"Расчет: {product1.price} * {product1.quantity} + "
        f"{product3.price} * {product3.quantity} = {total_cost}"
    )

    # Тестирование сеттера цены
    print("\n--- Тестирование сеттера цены ---")
    print(f"Текущая цена смартфона: {product1.price} руб.")
    product1.price = 45000.0
    print(f"Новая цена смартфона: {product1.price} руб.")
    product1.price = -5000.0  # попытка установить отрицательную цену

    # Тестирование класс-метода new_product
    print("\n--- Тестирование класс-метода new_product ---")
    product_data = {
        'name': 'Планшет',
        'description': 'Удобный планшет для работы',
        'price': 35000.0,
        'quantity': 8
    }
    tablet = Product.new_product(product_data)
    electronics.add_product(tablet)
    print(f"Добавлен новый продукт: {tablet.name}")
    print(electronics.products)

    # Пример загрузки из JSON
    try:
        categories = load_categories_from_json("data/products.json")
        for category in categories:
            print(f"\nЗагружена категория: {category.name}")
            print(category.products)
            print(f"Строковое представление: {category}")
    except FileNotFoundError:
        print("\nФайл products.json не найден")
    except json.JSONDecodeError:
        print("\nОшибка при чтении JSON файла")


if __name__ == "__main__":
    main()
