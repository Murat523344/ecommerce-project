"""Модуль с классами Product и Category для e-commerce платформы."""

from typing import List, Dict, Any


class Product:
    """Класс для представления продукта."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """
        Инициализация продукта.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self._price = price  # приватный атрибут
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер для цены с проверкой.

        Args:
            value: Новое значение цены
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> 'Product':
        """
        Класс-метод для создания продукта из словаря.

        Args:
            product_data: Словарь с данными продукта

        Returns:
            Экземпляр класса Product
        """
        return cls(
            name=product_data.get('name', ''),
            description=product_data.get('description', ''),
            price=product_data.get('price', 0.0),
            quantity=product_data.get('quantity', 0)
        )


class Category:
    """Класс для представления категории товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: List[Product]
    ) -> None:
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список продуктов в категории
        """
        self.name = name
        self.description = description
        self.__products = products  # приватный атрибут

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        """
        Геттер для списка продуктов. Возвращает строку с информацией.

        Returns:
            Строка с продуктами в формате
            "Название продукта, X руб. Остаток: X шт.\n"
        """
        if not self.__products:
            return ""

        result = []
        for product in self.__products:
            result.append(
                f"{product.name}, {product.price} руб. Остаток: "
                f"{product.quantity} шт.\n"
            )
        return "".join(result)

    def add_product(self, product: Product) -> None:
        """
        Добавление продукта в категорию.

        Args:
            product: Объект класса Product для добавления
        """
        self.__products.append(product)
        Category.product_count += 1
