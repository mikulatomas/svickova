import typing
import json

from dataclasses import dataclass

from .enums import Category, Special

@dataclass
class Meal:
    name: str
    category: "Category"
    special: typing.List["Special"]
    count: typing.Union[float, int]
    price: float

    def __iter__(self):
        count = self.count
        price = self.price
        
        if count == float("inf") or count == float("-inf"):
            count = 0

        if price == float("inf") or price == float("-inf"):
            price = 0

        yield from {
            "name": self.name,
            "category": self.category.value,
            "special": [s.value for s in self.special],
            "count": count,
            "price": price,
        }.items()

    def __str__(self) -> str:
        return json.dumps(dict(self), ensure_ascii=False)

    def to_json(self):
        return dict(self)
