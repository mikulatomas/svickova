import pathlib

from datetime import date

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from .engine import download_menu
from .enums import Canteen


def cli():
    options = Options()
    options.headless = True
    service_path = pathlib.Path("/usr/local/bin/chromedriver")
    service = Service(str(service_path))
    driver = webdriver.Chrome(
        service=service,
        options=options,
    )

    print(download_menu(Canteen.LISTOPAD_17, date.today(), driver))
