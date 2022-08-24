import math
from typing import Any
from urllib.parse import urlencode
from datetime import date, datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .meal import Meal
from .enums import Category, Special, Canteen

URL = "https://menza.upol.cz/WebKredit2/Ordering/Menu?"


def parse_menu(menu_element: Any) -> list["Meal"]:
    meals: list["Meal"] = []

    category = ""
    for elem in menu_element.find_elements(By.TAG_NAME, "tr"):
        subelements = elem.find_elements(By.TAG_NAME, "td")

        if len(subelements) < 2:
            category = next(iter(elem.text.split(" - ")))
        else:
            specials: list[str] = [
                elem.get_attribute("title")
                for elem in subelements[1].find_elements(By.TAG_NAME, "img")
            ]
            name: str = (
                subelements[3]
                .find_element(By.TAG_NAME, "span")
                .text.removeprefix("BEZLEP ")
            )
            count: str | int | float = subelements[4].text
            count = int(count) if count else math.inf
            price = float(
                subelements[5].text.removesuffix("Kč").strip().replace(",", ".")
            )

            meals.append(
                Meal(
                    name,
                    Category(category),
                    [Special(special) for special in specials],
                    count,
                    price,
                )
            )

    return meals


def download_menu(
    canteen: "Canteen",
    date: date | datetime,
    driver: "WebDriver",
) -> list["Meal"]:
    get_vars = {"canteen": canteen, "dateFrom": date, "dateTo": date}
    url = f"{URL}{urlencode(get_vars)}"

    driver.get(url)  # type: ignore

    xpath = "/html/body/div/main/div/div[2]/section/article/div/div/table/tbody"

    menu_element: Any = WebDriverWait(driver, 10).until(  # type: ignore
        EC.presence_of_element_located((By.XPATH, xpath))  # type: ignore
    )

    return parse_menu(menu_element)
