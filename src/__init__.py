"""E-commerce core package."""

from src.classes import Product, Category
from src.utils import load_categories_from_json

__all__ = ["Product", "Category", "load_categories_from_json"]
