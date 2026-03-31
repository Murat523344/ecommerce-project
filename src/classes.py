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
