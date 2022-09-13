import math
import datetime
import dateutil.tz
import requests
import json

from typing import Dict
from urllib.parse import urlencode

from .meal import Meal
from .enums import Category, Special, Canteen

API = "https://menza.upol.cz/webkredit2/Api/Ordering/Menu?"


def parse_menu(data: Dict) -> list["Meal"]:
    meals: list["Meal"] = []

    special_names = {special["id"]: special["name"] for special in data["pictograms"]}

    for group in data["groups"]:
        category = Category(group["mealKindName"])
        for meal in group["rows"]:
            meal = meal["item"]

            name = meal["mealName"].removeprefix("BEZLEP ")
            specials = meal["pictograms"] if meal["pictograms"] else []
            count = meal["countAvailable"] if meal["countAvailable"] else math.inf

            price = meal["price2"]
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
    date: datetime.datetime,
) -> list["Meal"]:
    date = date.replace(hour=0, minute=0, second=0, microsecond=0).astimezone(
        dateutil.tz.tzutc()
    )

    get_vars = {"CanteenId": canteen.value, "Dates": date.strftime("%Y-%m-%dT%H:%M:%SZ")}
    url = f"{API}{urlencode(get_vars)}"

    data = json.loads(requests.get(url).content)

    return parse_menu(data)
