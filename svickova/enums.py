from enum import Enum

class Category(str, Enum):
    SOUP: str = "Polévky, saláty"
    DAILY_OFFER: str = "Hotovky"
    SPECIALS: str = "Minutky"
    PIZZA: str = "Pizza"

class Special(str, Enum):
    FRY: str = "Smažené jídlo"
    VEG: str = "Vegetariánské jídlo"
    GLUTEN: str = "Bezlepkové jídlo"

class Canteen(int, Enum):
    LISTOPAD_17: int = 1
    KRIZKOVSKEHO: int = 2
    SMERALOVA: int = 3
    LEKARSKA_FAKULTA: int = 4
    NEREDIN: int = 6
    HOLICE: int = 13
