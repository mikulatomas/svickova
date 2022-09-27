from enum import Enum, IntEnum


class Category(str, Enum):
    SOUP = "Polévky, saláty"
    DAILY_OFFER = "Hotovky"
    SPECIALS = "Minutky"
    PIZZA = "Pizza"
    UNKNOWN = ""


class Special(str, Enum):
    FRY = "Smažené jídlo"
    VEGAN = "Vegan"
    VEGETARIAN = "Vegetariánské jídlo"
    GLUTEN = "Bezlepkové jídlo"


class Canteen(IntEnum):
    LISTOPAD_17 = 1
    KRIZKOVSKEHO = 2
    SMERALOVA = 3
    LEKARSKA_FAKULTA = 4
    NEREDIN = 6
    HOLICE = 13
