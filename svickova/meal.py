import typing
from dataclasses import dataclass

from .enums import Category, Special

@dataclass
class Meal:
    name: str
    category: "Category"
    special: typing.List["Special"]
    count: typing.Union[float, int]
    price: float
