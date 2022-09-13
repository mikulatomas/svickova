import datetime
import dateutil.tz

from .engine import download_menu
from .enums import Canteen


def cli():
    print(
        download_menu(
            Canteen.LISTOPAD_17, datetime.datetime.now(dateutil.tz.gettz("Prague"))
        )
    )
