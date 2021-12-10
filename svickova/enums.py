from enum import Enum

class Category(Enum):
    SOUP = "Polévky, saláty"
    DAILY_OFFER = "Hotovky"
    SPECIALS = "Minutky"

class Special(Enum):
    FRY = "Smažené jídlo"
    VEG = "Vegetariánské jídlo"
    GLUTEN = "Bezlepkové jídlo"

class Canteen(Enum):
    LISTOPAD_17 = 1
    KRIZKOVSKEHO = 2
    SMERALOVA = 3
    LEKARSKA_FAKULTA = 4
    NEREDIN = 6
    HOLICE = 13

