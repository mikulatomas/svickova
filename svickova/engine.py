import json
import dateutil.tz
from typing import Any
from datetime import datetime

from urllib.parse import urlencode
from urllib.request import urlopen

from .meal import Meal
from .enums import Category, Special, Canteen

API = "https://menza.upol.cz/webkredit2/Api/Ordering/Menu?"


def meal_name_adjustment(meal_name: str) -> str:
    name: str = meal_name
    for prefix in ["BEZLEP", "PIZZA"]:
        name = name.removeprefix(f"{prefix} ")
    name = name.capitalize()

    return name


def parse_menu(data: dict[str, Any]) -> list["Meal"]:
    meals: list["Meal"] = []

    special_names = {special["id"]: special["name"] for special in data["pictograms"]}

    for group in data["groups"]:
        category = Category(group["mealKindName"])
        for meal in group["rows"]:
            meal = meal["item"]

            name = meal_name_adjustment(meal["mealName"])
            specials: list[str] = meal["pictograms"] if meal["pictograms"] else []
            count: int = meal["countAvailable"] if meal["countAvailable"] else 0

            price: float = meal["price2"]
            meals.append(
                Meal(
                    name,
                    category,
                    [Special(special_names[idx]) for idx in specials],
                    count,
                    price,
                )
            )

    return meals


def download_menu(
    canteen: "Canteen",
    date: datetime,
) -> list["Meal"]:
    date = date.replace(hour=0, minute=0, second=0, microsecond=0).astimezone(
        dateutil.tz.tzutc()
    )

    get_vars = {
        "CanteenId": canteen.value,
        "Dates": date.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    url = f"{API}{urlencode(get_vars)}"

    data = json.loads(urlopen(url).read())

    return parse_menu(data)
