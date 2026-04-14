"""Модуль с классами Product и Category для e-commerce платформы."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other: 'BaseProduct') -> float:
        """Абстрактный метод сложения продуктов."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер цены."""
        pass


class MixinRepr:
    """Миксин для вывода информации о созданном объекте."""

    def __init__(self, *args, **kwargs) -> None:
        """Инициализация миксина с выводом информации об объекте."""
        super().__init__(*args, **kwargs)
        print(f"Создан объект: {self.__repr__()}")

    def __repr__(self) -> str:
        """
        Магический метод для отображения информации об объекте.

        Returns:
            Строка с информацией о классе и параметрах объекта
        """
        attributes = []
        for key, value in self.__dict__.items():
            # Пропускаем приватные атрибуты
            if not key.startswith('_'):
                attributes.append(f"{key}={repr(value)}")
        return f"{self.__class__.__name__}({', '.join(attributes)})"


class Product(BaseProduct, MixinRepr):
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

        Raises:
            ValueError: Если количество товара равно нулю
        """
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self._price = price  # приватный атрибут
        self.quantity = quantity
        # Вызов миксина происходит автоматически через super()
        super().__init__()

    def __str__(self) -> str:
        """
        Строковое представление продукта.

        Returns:
            Строка в формате: "Название продукта, X руб. Остаток: X шт."
        """
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        """
        Магический метод сложения двух продуктов.

        Args:
            other: Другой объект Product

        Returns:
            Сумма произведений цены на количество для двух продуктов

        Raises:
            TypeError: Если объекты разных классов
        """
        if type(self) is not type(other):
            raise TypeError(
                f"Нельзя складывать объекты разных классов: "
                f"{type(self).__name__} и {type(other).__name__}"
            )
        return (self._price * self.quantity) + (other._price * other.quantity)

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


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Инициализация смартфона.

        Args:
            name: Название смартфона
            description: Описание смартфона
            price: Цена смартфона
            quantity: Количество на складе
            efficiency: Производительность
            model: Модель смартфона
            memory: Объем встроенной памяти (ГБ)
            color: Цвет смартфона
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Инициализация газонной травы.

        Args:
            name: Название травы
            description: Описание травы
            price: Цена травы
            quantity: Количество на складе
            country: Страна-производитель
            germination_period: Срок прорастания
            color: Цвет травы
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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

    def __str__(self) -> str:
        """
        Строковое представление категории.

        Returns:
            Строка в формате: "Название категории, количество продуктов: X шт."
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

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
            result.append(str(product) + "\n")
        return "".join(result)

    def add_product(self, product: Product) -> None:
        """
        Добавление продукта в категорию.

        Args:
            product: Объект класса Product или его наследников

        Raises:
            TypeError: Если product не является экземпляром Product или его наследником
        """
        if not isinstance(product, Product):
            raise TypeError(
                f"Можно добавлять только объекты Product или его наследников. "
                f"Получен: {type(product).__name__}"
            )
        self.__products.append(product)
        Category.product_count += 1

    def average_price(self) -> float:
        """
        Подсчет среднего ценника всех товаров в категории.

        Returns:
            Средняя цена всех товаров в категории.
            Если товаров нет, возвращает 0.
        """
        if not self.__products:
            return 0.0

        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0
