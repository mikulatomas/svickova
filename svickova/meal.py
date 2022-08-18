from dataclasses import dataclass

from .enums import Category, Special


@dataclass
class Meal:
    name: str
    category: "Category"
    special: list["Special"]
    count: float | int
    price: float
