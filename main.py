"""Главный модуль e-commerce приложения."""

from src.classes import Product, Category, Smartphone, LawnGrass, BaseProduct
from src.utils import load_categories_from_json
import json


def main() -> None:
    """Основная функция приложения."""
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ АБСТРАКТНОГО КЛАССА И МИКСИНА")
    print("=" * 60)

    # Создание тестовых продуктов (миксин автоматически выводит информацию)
    print("\n--- Создание продуктов (миксин выводит информацию) ---")
    product1 = Product("Смартфон", "Мощный смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой ноутбук", 80000.0, 5)

    # Создание смартфона
    smartphone = Smartphone(
        "iPhone 15 Pro",
        "Флагманский смартфон Apple",
        99999.0,
        8,
        "Высокая",
        "15 Pro",
        256,
        "черный"
    )

    # Создание газонной травы
    grass = LawnGrass(
        "Газонная трава 'Изумруд'",
        "Смесь для идеального газона",
        1500.0,
        50,
        "Россия",
        "7-14 дней",
        "зеленый"
    )

    # Проверка принадлежности к абстрактному классу
    print("\n--- Проверка наследования от BaseProduct ---")
    print(f"product1 является BaseProduct: {isinstance(product1, BaseProduct)}")
    print(f"smartphone является BaseProduct: {isinstance(smartphone, BaseProduct)}")
    print(f"grass является BaseProduct: {isinstance(grass, BaseProduct)}")

    # Создание категории с продуктами
    electronics = Category("Электроника", "Различные электронные устройства", [])
    garden = Category("Садоводство", "Товары для сада и огорода", [])

    # Добавление продуктов в категории
    electronics.add_product(product1)
    electronics.add_product(product2)
    electronics.add_product(smartphone)
    garden.add_product(grass)

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ КЛАССОВ-НАСЛЕДНИКОВ")
    print("=" * 60)

    print(f"\nКатегория: {electronics.name}")
    print(f"Количество категорий: {Category.category_count}")
    print(f"Количество продуктов: {Category.product_count}")

    print("\nТовары в категории 'Электроника':")
    print(electronics.products)

    print(f"\nКатегория: {garden.name}")
    print(garden.products)

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ МАГИЧЕСКИХ МЕТОДОВ")
    print("=" * 60)

    # Тестирование строкового представления
    print(f"\nПродукт (обычный): {product1}")
    print(f"Смартфон: {smartphone}")
    print(f"Газонная трава: {grass}")
    print(f"Категория Электроника: {electronics}")
    print(f"Категория Садоводство: {garden}")

    # Тестирование сложения
    print("\n--- Тестирование __add__ ---")
    total_cost = product1 + product2
    print(f"Стоимость товаров на складе (продукты): {total_cost} руб.")

    # Сложение смартфонов
    smartphone2 = Smartphone(
        "Samsung Galaxy S24",
        "Флагманский смартфон Samsung",
        89999.0,
        5,
        "Высокая",
        "S24",
        256,
        "фиолетовый"
    )
    total_smartphones = smartphone + smartphone2
    print(f"Стоимость смартфонов на складе: {total_smartphones} руб.")

    # Попытка сложения разных типов (вызовет ошибку)
    print("\n--- Попытка сложения разных типов ---")
    try:
        result = product1 + smartphone
        print(f"Результат: {result}")
    except TypeError as e:
        print(f"Ошибка (ожидаемо): {e}")

    # Тестирование сеттера цены
    print("\n--- Тестирование сеттера цены ---")
    print(f"Текущая цена смартфона: {smartphone.price} руб.")
    smartphone.price = 85000.0
    print(f"Новая цена смартфона: {smartphone.price} руб.")
    smartphone.price = -5000.0  # попытка установить отрицательную цену

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

    # Пример загрузки из JSON
    print("\n--- Загрузка из JSON ---")
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
