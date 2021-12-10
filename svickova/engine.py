import urllib
import math

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .meal import Meal
from .enums import Category, Special, Canteen

URL = "https://menza.upol.cz/WebKredit2/Ordering/Menu?"

def parse_menu(menu_element):
    meals = []

    for elem in menu_element.find_elements(By.TAG_NAME, "tr"):
        subelements = elem.find_elements(By.TAG_NAME, "td")

        if len(subelements) < 2:
            category = next(iter(elem.text.split(" - ")))    
        else:
            specials = [elem.get_attribute("title") for elem in subelements[1].find_elements(By.TAG_NAME, "img")]
            name = subelements[3].find_element(By.TAG_NAME, "span").text.removeprefix("BEZLEP ")
            count_text = subelements[4].text
            count =  int(count_text) if count_text else math.inf
            price = float(subelements[5].text.removesuffix("Kč").strip().replace(",", "."))

            meals.append(Meal(name, Category(category), [Special(special) for special in specials], count, price))
    
    return meals


def download_menu(canteen: "Canteen", date, driver):
    get_vars = {"canteen": canteen, "dateFrom": date, "dateTo": date}
    url = f"{URL}{urllib.parse.urlencode(get_vars)}"

    driver.get(url)

    xpath = "/html/body/div/main/div/div[2]/section/article/div/div/table/tbody"

    menu_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

    return parse_menu(menu_element)


    
