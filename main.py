"""Главный модуль e-commerce приложения."""

from src.classes import Product, Category, Smartphone, LawnGrass
from src.utils import load_categories_from_json
import json


def main() -> None:
    """Основная функция приложения."""
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ОБРАБОТКИ ИСКЛЮЧЕНИЙ")
    print("=" * 60)

    # Тестирование создания продукта с нулевым количеством
    print("\n--- Создание продукта с нулевым количеством ---")
    try:
        bad_product = Product("Бракованный", "Не должен создаться", 100.0, 0)
        print(f"Создан продукт: {bad_product}")
    except ValueError as e:
        print(f"Ошибка (ожидаемо): {e}")

    # Создание продуктов с корректным количеством
    print("\n--- Создание продуктов ---")
    try:
        product1 = Product("Смартфон", "Мощный смартфон", 50000.0, 10)
        product2 = Product("Ноутбук", "Игровой ноутбук", 80000.0, 5)
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
        grass = LawnGrass(
            "Газонная трава 'Изумруд'",
            "Смесь для идеального газона",
            1500.0,
            50,
            "Россия",
            "7-14 дней",
            "зеленый"
        )
        print("Все продукты успешно созданы")
    except ValueError as e:
        print(f"Ошибка при создании продукта: {e}")

    # Создание категорий и добавление продуктов
    electronics = Category("Электроника", "Различные электронные устройства", [])
    garden = Category("Садоводство", "Товары для сада и огорода", [])

    electronics.add_product(product1)
    electronics.add_product(product2)
    electronics.add_product(smartphone)
    garden.add_product(grass)

    # Тестирование метода подсчета средней цены
    print("\n--- Подсчет средней цены в категориях ---")
    avg_electronics = electronics.average_price()
    avg_garden = garden.average_price()
    print(f"Средняя цена в категории 'Электроника': {avg_electronics:.2f} руб.")
    print(f"Средняя цена в категории 'Садоводство': {avg_garden:.2f} руб.")

    # Создание пустой категории для теста
    empty_category = Category("Пустая", "Категория без товаров", [])
    print(f"Средняя цена в пустой категории: {empty_category.average_price():.2f} руб.")

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ОСТАЛЬНОГО ФУНКЦИОНАЛА")
    print("=" * 60)

    print(f"\nКатегория: {electronics.name}")
    print(f"Количество категорий: {Category.category_count}")
    print(f"Количество продуктов: {Category.product_count}")

    print("\nТовары в категории 'Электроника':")
    print(electronics.products)

    print(f"\nКатегория: {garden.name}")
    print(garden.products)

    # Тестирование строкового представления
    print(f"\nПродукт (обычный): {product1}")
    print(f"Смартфон: {smartphone}")
    print(f"Газонная трава: {grass}")

    # Тестирование сложения
    print("\n--- Тестирование __add__ ---")
    total_cost = product1 + product2
    print(f"Стоимость товаров на складе (продукты): {total_cost} руб.")

    # Попытка сложения разных типов
    print("\n--- Попытка сложения разных типов ---")
    try:
        result = product1 + smartphone
        print(f"Результат: {result}")
    except TypeError as e:
        print(f"Ошибка (ожидаемо): {e}")

    # Пример загрузки из JSON
    print("\n--- Загрузка из JSON ---")
    try:
        categories = load_categories_from_json("data/products.json")
        for category in categories:
            print(f"\nЗагружена категория: {category.name}")
            print(category.products)
            print(f"Строковое представление: {category}")
            print(f"Средняя цена: {category.average_price():.2f} руб.")
    except FileNotFoundError:
        print("\nФайл products.json не найден")
    except json.JSONDecodeError:
        print("\nОшибка при чтении JSON файла")


if __name__ == "__main__":
    main()
